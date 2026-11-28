"""Lectura CSV y validación de comparables."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd

from calculadora_precio.modelos import Comparable

CSV_COLUMNS = [
    "precio",
    "m2",
    "tipo_precio",
    "fuente",
    "url",
    "fecha",
    "barrio",
    "planta",
    "ascensor",
    "estado",
    "orientacion",
    "terraza",
    "garaje",
    "trastero",
    "notas",
]


def leer_comparables_csv(ruta: str | Path) -> list[Comparable]:
    """Lee un CSV de comparables (UTF-8, separador coma)."""
    path = Path(ruta)
    if not path.exists():
        raise FileNotFoundError(f"No se encuentra el CSV: {path}")

    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    faltan = [c for c in ("precio", "m2", "tipo_precio", "fuente", "fecha", "barrio", "planta", "ascensor", "estado", "orientacion") if c not in df.columns]
    if faltan:
        raise ValueError(f"CSV sin columnas obligatorias: {', '.join(faltan)}")

    comparables: list[Comparable] = []
    for i, row in df.iterrows():
        datos = {col: (row[col] if col in df.columns else "") for col in CSV_COLUMNS}
        # Campos opcionales vacíos → None / False
        if not str(datos.get("url") or "").strip():
            datos["url"] = None
        if not str(datos.get("notas") or "").strip():
            datos["notas"] = None
        for b in ("terraza", "garaje", "trastero"):
            if not str(datos.get(b) or "").strip():
                datos[b] = "no"
        datos["id"] = f"fila-{int(i) + 2}"  # +2: cabecera + 1-index
        try:
            comparables.append(Comparable.model_validate(datos))
        except Exception as exc:  # noqa: BLE001
            raise ValueError(f"Error en fila CSV {int(i) + 2}: {exc}") from exc

    return validar_lista_comparables(comparables)


def validar_lista_comparables(comparables: list[Comparable]) -> list[Comparable]:
    """Valida cantidad y duplicados (3–10)."""
    n = len(comparables)
    if n < 3:
        raise ValueError(f"Se necesitan al menos 3 comparables (hay {n}).")
    if n > 10:
        raise ValueError(f"Máximo 10 comparables (hay {n}).")

    vistos_url: set[str] = set()
    vistos_clave: set[tuple] = set()
    for c in comparables:
        if c.url:
            key_url = c.url.strip().casefold()
            if key_url in vistos_url:
                raise ValueError(f"Comparable duplicado (misma URL): {c.url}")
            vistos_url.add(key_url)
        clave = (round(c.precio, 2), round(c.m2, 2), c.barrio_norm)
        if clave in vistos_clave:
            raise ValueError(
                f"Comparable duplicado (mismo precio+m²+barrio): {c.precio} €, {c.m2} m², {c.barrio}"
            )
        vistos_clave.add(clave)

    return comparables


def meses_entre(fecha: date, referencia: date) -> float:
    """Antigüedad aproximada en meses."""
    dias = (referencia - fecha).days
    return dias / 30.4375
