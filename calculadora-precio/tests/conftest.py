"""Fixtures compartidas (datos ficticios)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from calculadora_precio.modelos import (
    Comparable,
    ConfigCoeficientes,
    Estado,
    Orientacion,
    TipoPrecio,
    Vivienda,
)

DATA_DIR = Path(__file__).parent / "data"
FECHA_REF = date(2026, 11, 28)


@pytest.fixture
def vivienda_base() -> Vivienda:
    return Vivienda(
        direccion="Calle Ejemplo 1",
        barrio="BarrioEjemplo",
        m2_construidos=90,
        m2_utiles=75,
        habitaciones=3,
        banos=2,
        planta=3,
        ascensor=True,
        estado=Estado.BUEN_ESTADO,
        orientacion=Orientacion.EXTERIOR,
        terraza=False,
        garaje=False,
        trastero=False,
    )


@pytest.fixture
def config_ejemplo() -> ConfigCoeficientes:
    return ConfigCoeficientes()


def _comp(
    precio: float,
    m2: float,
    *,
    tipo: TipoPrecio = TipoPrecio.CIERRE,
    barrio: str = "BarrioEjemplo",
    planta: int = 2,
    ascensor: bool = True,
    estado: Estado = Estado.BUEN_ESTADO,
    orientacion: Orientacion = Orientacion.EXTERIOR,
    fecha: date = date(2026, 10, 1),
    url: str | None = None,
) -> Comparable:
    return Comparable(
        precio=precio,
        m2=m2,
        tipo_precio=tipo,
        fuente="Test",
        fecha=fecha,
        barrio=barrio,
        planta=planta,
        ascensor=ascensor,
        estado=estado,
        orientacion=orientacion,
        url=url,
    )


@pytest.fixture
def tres_comparables() -> list[Comparable]:
    return [
        _comp(200000, 100, url="https://example.com/1"),
        _comp(210000, 105, fecha=date(2026, 9, 15), url="https://example.com/2"),
        _comp(190000, 95, fecha=date(2026, 10, 20), url="https://example.com/3"),
    ]


@pytest.fixture
def cinco_comparables_con_extremo() -> list[Comparable]:
    return [
        _comp(200000, 100, url="https://example.com/1"),
        _comp(205000, 100, fecha=date(2026, 9, 1), url="https://example.com/2"),
        _comp(198000, 100, fecha=date(2026, 9, 10), url="https://example.com/3"),
        _comp(202000, 100, fecha=date(2026, 10, 5), url="https://example.com/4"),
        _comp(400000, 100, fecha=date(2026, 10, 15), url="https://example.com/extremo"),
    ]
