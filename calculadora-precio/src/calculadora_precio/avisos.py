"""Reglas de avisos del resultado."""

from __future__ import annotations

from calculadora_precio.modelos import ComparableProcesado


def generar_avisos(
    *,
    usados: list[ComparableProcesado],
    descartados: list[ComparableProcesado],
    n_anuncio: int,
    n_cierre: int,
    eur_m2_valores: list[float],
) -> list[str]:
    avisos: list[str] = []

    avisos.append(
        "Esto es una estimación orientativa por comparables. "
        "No es una tasación oficial ni sustituye la visita al inmueble."
    )

    n = len(usados)
    if n < 5:
        avisos.append(
            f"Solo hay {n} comparables usados: el rango es poco fiable."
        )

    if n_anuncio and n_cierre == 0:
        avisos.append(
            "Todos los comparables usados son precios de anuncio, no de cierre. "
            "Se aplicó el descuento anuncio→cierre (EJEMPLO, AJUSTAR)."
        )
    elif n_anuncio and n_cierre:
        avisos.append(
            f"Mezcla de precios: {n_anuncio} anuncio(s) y {n_cierre} cierre(s)."
        )

    por_antiguedad = [
        d for d in descartados if d.motivo_descarte and "antigüedad" in d.motivo_descarte
    ]
    if por_antiguedad:
        avisos.append(
            f"Se excluyeron {len(por_antiguedad)} comparable(s) por antigüedad máxima."
        )

    por_barrio = [
        d for d in descartados if d.motivo_descarte and "barrio" in d.motivo_descarte
    ]
    if por_barrio:
        avisos.append(
            f"Se excluyeron {len(por_barrio)} comparable(s) por barrio distinto."
        )

    por_iqr = [d for d in descartados if d.motivo_descarte and "IQR" in d.motivo_descarte]
    if por_iqr:
        avisos.append(f"Se descartaron {len(por_iqr)} extremo(s) por IQR.")

    if len(eur_m2_valores) >= 2:
        media = sum(eur_m2_valores) / len(eur_m2_valores)
        if media > 0:
            dispersion = (max(eur_m2_valores) - min(eur_m2_valores)) / media
            if dispersion > 0.25:
                avisos.append(
                    f"Alta dispersión en €/m² normalizados "
                    f"(rango relativo {dispersion:.0%}): interpreta el resultado con cautela."
                )

    return avisos
