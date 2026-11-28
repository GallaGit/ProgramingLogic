"""CSV y validación de lista."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from calculadora_precio.comparables import leer_comparables_csv, validar_lista_comparables
from calculadora_precio.modelos import Comparable, Estado, Orientacion, TipoPrecio

DATA = Path(__file__).parent / "data"


def test_leer_csv_ok():
    comps = leer_comparables_csv(DATA / "comparables_ok.csv")
    assert 3 <= len(comps) <= 10
    assert comps[0].eur_m2 > 0


def test_menos_de_tres_falla(tres_comparables):
    with pytest.raises(ValueError, match="al menos 3"):
        validar_lista_comparables(tres_comparables[:2])


def test_mas_de_diez_falla(tres_comparables):
    muchos = []
    for i in range(11):
        c = tres_comparables[0].model_copy(
            update={
                "precio": 100000 + i * 1000,
                "url": f"https://example.com/{i}",
                "fecha": date(2026, 10, 1),
            }
        )
        muchos.append(c)
    with pytest.raises(ValueError, match="Máximo 10"):
        validar_lista_comparables(muchos)


def test_duplicado_url_falla(tres_comparables):
    dup = tres_comparables[0].model_copy(update={"precio": 999999})
    with pytest.raises(ValueError, match="URL"):
        validar_lista_comparables([*tres_comparables, dup])
