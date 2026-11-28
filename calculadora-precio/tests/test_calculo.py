"""Núcleo de cálculo con datos ficticios."""

from __future__ import annotations

from datetime import date

import pytest

from calculadora_precio.calculo import estimar_precio
from calculadora_precio.modelos import ConfigCoeficientes, TipoPrecio

FECHA_REF = date(2026, 11, 28)


def test_estimacion_basica(vivienda_base, tres_comparables, config_ejemplo):
    r = estimar_precio(
        vivienda_base, tres_comparables, config_ejemplo, fecha_referencia=FECHA_REF
    )
    assert r.precio_minimo < r.precio_recomendado < r.precio_maximo
    assert r.eur_m2_mediana > 0
    assert r.eur_m2_medio > 0
    assert len(r.comparables_usados) == 3
    assert r.explicacion
    assert any("tasación" in a.lower() or "orientativa" in a.lower() for a in r.avisos)


def test_sin_iqr_con_menos_de_cinco(vivienda_base, tres_comparables, config_ejemplo):
    r = estimar_precio(
        vivienda_base, tres_comparables, config_ejemplo, fecha_referencia=FECHA_REF
    )
    assert not any(
        d.motivo_descarte and "IQR" in d.motivo_descarte for d in r.comparables_descartados
    )
    assert any("no se aplica descarte IQR" in e for e in r.explicacion)


def test_iqr_descarta_extremo(vivienda_base, cinco_comparables_con_extremo, config_ejemplo):
    r = estimar_precio(
        vivienda_base,
        cinco_comparables_con_extremo,
        config_ejemplo,
        fecha_referencia=FECHA_REF,
    )
    assert any(
        d.motivo_descarte and "IQR" in d.motivo_descarte for d in r.comparables_descartados
    )
    assert len(r.comparables_usados) >= 3
    # El extremo a 4000 €/m² no debe tirar la mediana cerca de 4000
    assert r.eur_m2_mediana < 3000


def test_coeficientes_neutros(vivienda_base, tres_comparables):
    cfg = ConfigCoeficientes(
        descuento_anuncio=1.0,
        margen_rango=0.0,
        planta_ascensor={
            "bajo_sin_ascensor": 1.0,
            "intermedia_sin_ascensor": 1.0,
            "intermedia_con_ascensor": 1.0,
            "alta_con_ascensor": 1.0,
            "tercera_o_mas_sin_ascensor": 1.0,
        },
        estado={"a_reformar": 1.0, "buen_estado": 1.0, "reformado": 1.0},
        orientacion={"exterior": 1.0, "interior": 1.0},
    )
    # Forzar todos cierre e iguales características
    comps = [
        c.model_copy(
            update={
                "tipo_precio": TipoPrecio.CIERRE,
                "planta": vivienda_base.planta,
                "ascensor": vivienda_base.ascensor,
                "estado": vivienda_base.estado,
                "orientacion": vivienda_base.orientacion,
                "precio": 200000 + i,  # evita duplicado precio+m²+barrio
                "m2": 100,
                "url": f"https://example.com/n{i}",
                "fecha": date(2026, 10, 1 + i),
            }
        )
        for i, c in enumerate(tres_comparables)
    ]
    r = estimar_precio(vivienda_base, comps, cfg, fecha_referencia=FECHA_REF)
    assert r.eur_m2_mediana == pytest.approx(2000.0, abs=0.1)
    assert r.precio_recomendado == pytest.approx(r.eur_m2_mediana * 90, abs=1)
    assert r.precio_minimo == r.precio_recomendado == r.precio_maximo


def test_descuento_anuncio(vivienda_base, tres_comparables):
    cfg = ConfigCoeficientes(
        descuento_anuncio=0.9,
        margen_rango=0.0,
        planta_ascensor={
            "bajo_sin_ascensor": 1.0,
            "intermedia_sin_ascensor": 1.0,
            "intermedia_con_ascensor": 1.0,
            "alta_con_ascensor": 1.0,
            "tercera_o_mas_sin_ascensor": 1.0,
        },
        estado={"a_reformar": 1.0, "buen_estado": 1.0, "reformado": 1.0},
        orientacion={"exterior": 1.0, "interior": 1.0},
    )
    comps = [
        c.model_copy(
            update={
                "tipo_precio": TipoPrecio.ANUNCIO,
                "planta": vivienda_base.planta,
                "ascensor": vivienda_base.ascensor,
                "estado": vivienda_base.estado,
                "orientacion": vivienda_base.orientacion,
                "precio": 200000 + i,
                "m2": 100,
                "url": f"https://example.com/a{i}",
                "fecha": date(2026, 10, 1 + i),
            }
        )
        for i, c in enumerate(tres_comparables)
    ]
    r = estimar_precio(vivienda_base, comps, cfg, fecha_referencia=FECHA_REF)
    assert r.eur_m2_mediana == pytest.approx(1800.0, abs=0.1)


def test_barrio_distinto_excluye(vivienda_base, tres_comparables, config_ejemplo):
    comps = list(tres_comparables)
    comps[0] = comps[0].model_copy(update={"barrio": "OtroBarrio"})
    # Siguen siendo 3 del mismo barrio? No — uno distinto → quedan 2 → error
    with pytest.raises(ValueError, match="barrio|al menos 3"):
        estimar_precio(vivienda_base, comps, config_ejemplo, fecha_referencia=FECHA_REF)


def test_antiguedad_excluye(vivienda_base, tres_comparables, config_ejemplo):
    comps = list(tres_comparables)
    comps.append(
        tres_comparables[0].model_copy(
            update={
                "precio": 220000,
                "fecha": date(2025, 1, 1),
                "url": "https://example.com/viejo",
            }
        )
    )
    # validar_lista permite 4; el viejo se descarta por antigüedad
    r = estimar_precio(vivienda_base, comps, config_ejemplo, fecha_referencia=FECHA_REF)
    assert any(
        d.motivo_descarte and "antigüedad" in d.motivo_descarte
        for d in r.comparables_descartados
    )


def test_base_construidos(vivienda_base, tres_comparables, config_ejemplo):
    r = estimar_precio(
        vivienda_base, tres_comparables, config_ejemplo, fecha_referencia=FECHA_REF
    )
    assert r.base_m2 == "construidos"
    assert r.m2_usados == vivienda_base.m2_construidos
