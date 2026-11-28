"""Núcleo de cálculo: sin I/O. Devuelve rango y explicación de ajustes."""

from __future__ import annotations

from datetime import date, datetime

import pandas as pd

from calculadora_precio.avisos import generar_avisos
from calculadora_precio.comparables import meses_entre, validar_lista_comparables
from calculadora_precio.modelos import (
    Comparable,
    ComparableProcesado,
    ConfigCoeficientes,
    Orientacion,
    Resultado,
    TipoPrecio,
    Vivienda,
)


def categoria_planta_ascensor(planta: int, ascensor: bool) -> str:
    if planta == 0 and not ascensor:
        return "bajo_sin_ascensor"
    if planta == 0 and ascensor:
        return "intermedia_con_ascensor"
    if 1 <= planta <= 2:
        return "intermedia_con_ascensor" if ascensor else "intermedia_sin_ascensor"
    # planta >= 3
    return "alta_con_ascensor" if ascensor else "tercera_o_mas_sin_ascensor"


def coeficiente_planta(cfg: ConfigCoeficientes, planta: int, ascensor: bool) -> float:
    cat = categoria_planta_ascensor(planta, ascensor)
    return float(getattr(cfg.planta_ascensor, cat))


def coeficiente_estado(cfg: ConfigCoeficientes, estado: str) -> float:
    return float(getattr(cfg.estado, estado))


def coeficiente_orientacion(cfg: ConfigCoeficientes, orientacion: Orientacion | str) -> float:
    key = orientacion.value if isinstance(orientacion, Orientacion) else orientacion
    return float(getattr(cfg.orientacion, key))


def factores_ajuste(
    cfg: ConfigCoeficientes,
    *,
    planta: int,
    ascensor: bool,
    estado: str,
    orientacion: Orientacion | str,
) -> dict[str, float]:
    return {
        "planta_ascensor": coeficiente_planta(cfg, planta, ascensor),
        "estado": coeficiente_estado(cfg, estado),
        "orientacion": coeficiente_orientacion(cfg, orientacion),
    }


def producto_factores(factores: dict[str, float]) -> float:
    p = 1.0
    for v in factores.values():
        p *= v
    return p


def calcular_extras(vivienda: Vivienda, cfg: ConfigCoeficientes) -> tuple[float, list[str]]:
    extras = 0.0
    detalle: list[str] = []
    ex = cfg.extras
    if vivienda.terraza:
        fijo = ex.terraza_fijo_eur
        por_m2 = 0.0
        if vivienda.m2_terraza and ex.terraza_por_m2_eur:
            por_m2 = vivienda.m2_terraza * ex.terraza_por_m2_eur
        extras += fijo + por_m2
        detalle.append(
            f"Terraza: +{fijo + por_m2:,.0f} € "
            f"(fijo {fijo:,.0f} € + m² {por_m2:,.0f} €; EJEMPLO, AJUSTAR)"
        )
    if vivienda.garaje:
        extras += ex.garaje_fijo_eur
        detalle.append(f"Garaje: +{ex.garaje_fijo_eur:,.0f} € (EJEMPLO, AJUSTAR)")
    if vivienda.trastero:
        extras += ex.trastero_fijo_eur
        detalle.append(f"Trastero: +{ex.trastero_fijo_eur:,.0f} € (EJEMPLO, AJUSTAR)")
    return extras, detalle


def _descartar_iqr(valores: list[float], k: float) -> tuple[float, float]:
    s = pd.Series(valores, dtype=float)
    q1 = float(s.quantile(0.25))
    q3 = float(s.quantile(0.75))
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


def estimar_precio(
    vivienda: Vivienda,
    comparables: list[Comparable],
    config: ConfigCoeficientes | None = None,
    *,
    fecha_referencia: date | None = None,
) -> Resultado:
    """
    Estima rango de precio (mín / recomendado / máx) a partir de comparables.

    Decisiones por defecto (revisables): base m² construidos, mediana central,
    IQR solo con >=5, mismo barrio, antigüedad máx. configurable.
    """
    cfg = config or ConfigCoeficientes()
    ref = fecha_referencia or date.today()
    validar_lista_comparables(comparables)

    m2_vivienda = (
        vivienda.m2_construidos if cfg.base_m2 == "construidos" else vivienda.m2_utiles
    )

    factores_viv = factores_ajuste(
        cfg,
        planta=vivienda.planta,
        ascensor=vivienda.ascensor,
        estado=vivienda.estado.value,
        orientacion=vivienda.orientacion,
    )
    prod_viv = producto_factores(factores_viv)

    procesados: list[ComparableProcesado] = []
    explicacion: list[str] = [
        "Método: €/m² de comparables → ajuste anuncio/cierre → "
        "normalización por coeficientes → mediana → extras → rango ± margen.",
        f"Base m²: {cfg.base_m2} ({m2_vivienda} m² de la vivienda).",
        f"Valor central: {cfg.valor_central} (la media se informa aparte).",
        (
            "Coeficientes de la vivienda "
            f"(planta/ascensor={factores_viv['planta_ascensor']:.3f}, "
            f"estado={factores_viv['estado']:.3f}, "
            f"orientación={factores_viv['orientacion']:.3f}; "
            "EJEMPLO, AJUSTAR)."
        ),
        f"Descuento anuncio→cierre: ×{cfg.descuento_anuncio:.3f} (EJEMPLO, AJUSTAR).",
        f"Antigüedad máxima: {cfg.antiguedad_max_meses} meses; zona = mismo barrio.",
    ]

    for c in comparables:
        factores_c = factores_ajuste(
            cfg,
            planta=c.planta,
            ascensor=c.ascensor,
            estado=c.estado.value,
            orientacion=c.orientacion,
        )
        prod_c = producto_factores(factores_c)
        eur_bruto = c.eur_m2
        if c.tipo_precio == TipoPrecio.ANUNCIO:
            eur_anuncio = eur_bruto * cfg.descuento_anuncio
        else:
            eur_anuncio = eur_bruto
        # Normalizar comparable hacia las características de la vivienda
        ratio = prod_viv / prod_c if prod_c else 1.0
        eur_norm = eur_anuncio * ratio

        motivo: str | None = None
        usado = True
        if c.barrio_norm != vivienda.barrio_norm:
            usado = False
            motivo = f"barrio distinto ('{c.barrio}' ≠ '{vivienda.barrio}')"
        else:
            ant = meses_entre(c.fecha, ref)
            if ant > cfg.antiguedad_max_meses:
                usado = False
                motivo = (
                    f"antigüedad {ant:.1f} meses > máximo {cfg.antiguedad_max_meses}"
                )
            elif ant < 0:
                usado = False
                motivo = "fecha futura respecto a la referencia"

        procesados.append(
            ComparableProcesado(
                comparable=c,
                eur_m2_bruto=eur_bruto,
                eur_m2_tras_anuncio=eur_anuncio,
                eur_m2_normalizado=eur_norm,
                factores=factores_c,
                usado=usado,
                motivo_descarte=motivo,
            )
        )

    candidatos = [p for p in procesados if p.usado]
    if len(candidatos) < 3:
        raise ValueError(
            f"Tras filtrar barrio/antigüedad quedan {len(candidatos)} comparables; "
            "se necesitan al menos 3 de la misma zona y recientes."
        )

    # IQR solo con >= 5
    if len(candidatos) >= 5:
        low, high = _descartar_iqr(
            [p.eur_m2_normalizado for p in candidatos], cfg.iqr_k
        )
        explicacion.append(
            f"Descarte IQR (k={cfg.iqr_k}): límites [{low:,.1f}, {high:,.1f}] €/m²."
        )
        for p in candidatos:
            if p.eur_m2_normalizado < low or p.eur_m2_normalizado > high:
                p.usado = False
                p.motivo_descarte = (
                    f"extremo IQR ({p.eur_m2_normalizado:,.1f} €/m² fuera de "
                    f"[{low:,.1f}, {high:,.1f}])"
                )
    else:
        explicacion.append(
            f"Solo {len(candidatos)} comparables candidatos: no se aplica descarte IQR."
        )

    usados = [p for p in procesados if p.usado]
    descartados = [p for p in procesados if not p.usado]

    if len(usados) < 3:
        raise ValueError(
            f"Tras descartar extremos quedan {len(usados)} comparables; "
            "se necesitan al menos 3."
        )

    serie = pd.Series([p.eur_m2_normalizado for p in usados], dtype=float)
    mediana = float(serie.median())
    media = float(serie.mean())
    eur_base = mediana if cfg.valor_central == "mediana" else media

    valor_base = eur_base * m2_vivienda
    extras, detalle_extras = calcular_extras(vivienda, cfg)
    recomendado = valor_base + extras
    minimo = recomendado * (1 - cfg.margen_rango)
    maximo = recomendado * (1 + cfg.margen_rango)

    explicacion.append(
        f"€/m² mediana={mediana:,.1f}; media={media:,.1f} (informativa). "
        f"Usado: {cfg.valor_central}={eur_base:,.1f}."
    )
    explicacion.append(
        f"Valor base = {eur_base:,.1f} €/m² × {m2_vivienda} m² = {valor_base:,.0f} €."
    )
    if detalle_extras:
        explicacion.extend(detalle_extras)
    else:
        explicacion.append("Extras: 0 € (valores EJEMPLO en 0; AJUSTAR en TOML).")
    explicacion.append(
        f"Rango con margen ±{cfg.margen_rango:.0%}: "
        f"{minimo:,.0f} – {recomendado:,.0f} – {maximo:,.0f} €."
    )

    n_anuncio = sum(1 for p in usados if p.comparable.tipo_precio == TipoPrecio.ANUNCIO)
    n_cierre = sum(1 for p in usados if p.comparable.tipo_precio == TipoPrecio.CIERRE)

    avisos = generar_avisos(
        usados=usados,
        descartados=descartados,
        n_anuncio=n_anuncio,
        n_cierre=n_cierre,
        eur_m2_valores=[p.eur_m2_normalizado for p in usados],
    )

    return Resultado(
        precio_minimo=round(minimo, 2),
        precio_recomendado=round(recomendado, 2),
        precio_maximo=round(maximo, 2),
        eur_m2_mediana=round(mediana, 2),
        eur_m2_medio=round(media, 2),
        valor_base=round(valor_base, 2),
        extras=round(extras, 2),
        m2_usados=m2_vivienda,
        base_m2=cfg.base_m2,
        comparables_usados=usados,
        comparables_descartados=descartados,
        n_anuncio=n_anuncio,
        n_cierre=n_cierre,
        coeficientes_aplicados=cfg.model_dump(),
        explicacion=explicacion,
        avisos=avisos,
        fecha_calculo=datetime.now(),
    )
