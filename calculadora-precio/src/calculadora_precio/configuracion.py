"""Carga y validación de coeficientes desde TOML."""

from __future__ import annotations

import tomllib
from pathlib import Path

from calculadora_precio.modelos import ConfigCoeficientes

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = PACKAGE_ROOT / "config" / "coeficientes.example.toml"


def cargar_config(ruta: str | Path | None = None) -> ConfigCoeficientes:
    """Carga coeficientes desde TOML. Sin ruta → ejemplo del paquete."""
    path = Path(ruta) if ruta else DEFAULT_CONFIG_PATH
    if not path.exists():
        raise FileNotFoundError(f"No se encuentra la configuración: {path}")
    with path.open("rb") as f:
        data = tomllib.load(f)
    return ConfigCoeficientes.model_validate(data)


def config_por_defecto() -> ConfigCoeficientes:
    """Valores EJEMPLO, AJUSTAR embebidos (sin leer fichero)."""
    return ConfigCoeficientes()
