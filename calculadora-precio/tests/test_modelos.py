"""Validación de modelos."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from calculadora_precio.modelos import Estado, Orientacion, Vivienda


def test_utiles_mayor_que_construidos_falla():
    with pytest.raises(ValidationError):
        Vivienda(
            direccion="x",
            barrio="y",
            m2_construidos=50,
            m2_utiles=60,
            habitaciones=1,
            banos=1,
            planta=1,
            ascensor=True,
            estado=Estado.BUEN_ESTADO,
            orientacion=Orientacion.EXTERIOR,
            terraza=False,
            garaje=False,
            trastero=False,
        )


def test_m2_cero_falla():
    with pytest.raises(ValidationError):
        Vivienda(
            direccion="x",
            barrio="y",
            m2_construidos=0,
            m2_utiles=0,
            habitaciones=1,
            banos=1,
            planta=0,
            ascensor="si",
            estado=Estado.BUEN_ESTADO,
            orientacion=Orientacion.EXTERIOR,
            terraza="no",
            garaje="no",
            trastero="no",
        )


def test_bool_si_no():
    v = Vivienda(
        direccion="x",
        barrio="Barrio",
        m2_construidos=80,
        m2_utiles=70,
        habitaciones=2,
        banos=1,
        planta=1,
        ascensor="si",
        estado="buen_estado",
        orientacion="exterior",
        terraza="no",
        garaje="si",
        trastero="no",
    )
    assert v.ascensor is True
    assert v.terraza is False
    assert v.garaje is True
