"""Calculadora de precio de venta por comparables (estimación orientativa)."""

from calculadora_precio.calculo import estimar_precio
from calculadora_precio.modelos import Comparable, Resultado, Vivienda

__all__ = ["Vivienda", "Comparable", "Resultado", "estimar_precio"]
__version__ = "0.2.0"
