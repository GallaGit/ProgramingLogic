"""Modelos pydantic: vivienda, comparable, resultado y configuración."""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator


class Estado(str, Enum):
    A_REFORMAR = "a_reformar"
    BUEN_ESTADO = "buen_estado"
    REFORMADO = "reformado"


class Orientacion(str, Enum):
    EXTERIOR = "exterior"
    INTERIOR = "interior"


class TipoPrecio(str, Enum):
    ANUNCIO = "anuncio"
    CIERRE = "cierre"


class CertificadoEnergetico(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    EN_TRAMITE = "en_tramite"
    DESCONOCIDO = "desconocido"


def _parse_bool(v: Any) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        s = v.strip().lower()
        if s in {"si", "sí", "true", "1", "yes"}:
            return True
        if s in {"no", "false", "0"}:
            return False
    raise ValueError(f"Valor booleano no válido: {v!r} (usa si/no)")


class Vivienda(BaseModel):
    direccion: str
    barrio: str
    m2_construidos: float = Field(gt=0)
    m2_utiles: float = Field(gt=0)
    habitaciones: int = Field(ge=0)
    banos: int = Field(ge=0)
    planta: int = Field(ge=0)
    ascensor: bool
    estado: Estado
    orientacion: Orientacion
    terraza: bool
    m2_terraza: float | None = Field(default=None, ge=0)
    garaje: bool
    trastero: bool
    anio_construccion: int | None = None
    certificado_energetico: CertificadoEnergetico = CertificadoEnergetico.DESCONOCIDO

    @field_validator("ascensor", "terraza", "garaje", "trastero", mode="before")
    @classmethod
    def _bool_fields(cls, v: Any) -> bool:
        return _parse_bool(v)

    @field_validator("barrio")
    @classmethod
    def _barrio_strip(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("barrio no puede estar vacío")
        return v

    @model_validator(mode="after")
    def _utiles_vs_construidos(self) -> Vivienda:
        if self.m2_utiles > self.m2_construidos:
            raise ValueError("m2_utiles no puede ser mayor que m2_construidos")
        return self

    @property
    def barrio_norm(self) -> str:
        return self.barrio.strip().casefold()


class Comparable(BaseModel):
    precio: float = Field(gt=0)
    m2: float = Field(gt=0)
    tipo_precio: TipoPrecio
    fuente: str
    fecha: date
    barrio: str
    planta: int = Field(ge=0)
    ascensor: bool
    estado: Estado
    orientacion: Orientacion
    url: str | None = None
    terraza: bool = False
    garaje: bool = False
    trastero: bool = False
    notas: str | None = None
    id: str | None = None

    @field_validator("ascensor", "terraza", "garaje", "trastero", mode="before")
    @classmethod
    def _bool_fields(cls, v: Any) -> bool:
        return _parse_bool(v)

    @field_validator("url", mode="before")
    @classmethod
    def _empty_url(cls, v: Any) -> str | None:
        if v is None or (isinstance(v, str) and not v.strip()):
            return None
        return str(v).strip()

    @field_validator("barrio")
    @classmethod
    def _barrio_strip(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("barrio no puede estar vacío")
        return v

    @property
    def eur_m2(self) -> float:
        return self.precio / self.m2

    @property
    def barrio_norm(self) -> str:
        return self.barrio.strip().casefold()


class ComparableProcesado(BaseModel):
    comparable: Comparable
    eur_m2_bruto: float
    eur_m2_tras_anuncio: float
    eur_m2_normalizado: float
    factores: dict[str, float]
    usado: bool
    motivo_descarte: str | None = None


class Resultado(BaseModel):
    precio_minimo: float
    precio_recomendado: float
    precio_maximo: float
    eur_m2_mediana: float
    eur_m2_medio: float
    valor_base: float
    extras: float
    m2_usados: float
    base_m2: str
    comparables_usados: list[ComparableProcesado]
    comparables_descartados: list[ComparableProcesado]
    n_anuncio: int
    n_cierre: int
    coeficientes_aplicados: dict[str, Any]
    explicacion: list[str]
    avisos: list[str]
    fecha_calculo: datetime


class PlantaAscensorCoef(BaseModel):
    bajo_sin_ascensor: float = 0.95
    intermedia_sin_ascensor: float = 0.97
    intermedia_con_ascensor: float = 1.00
    alta_con_ascensor: float = 1.03
    tercera_o_mas_sin_ascensor: float = 0.93


class EstadoCoef(BaseModel):
    a_reformar: float = 0.85
    buen_estado: float = 1.00
    reformado: float = 1.08


class OrientacionCoef(BaseModel):
    exterior: float = 1.00
    interior: float = 0.92


class ExtrasCoef(BaseModel):
    terraza_fijo_eur: float = 0.0
    terraza_por_m2_eur: float = 0.0
    garaje_fijo_eur: float = 0.0
    trastero_fijo_eur: float = 0.0


class ConfigCoeficientes(BaseModel):
    """Parámetros configurables. Valores por defecto = EJEMPLO, AJUSTAR."""

    base_m2: str = "construidos"
    valor_central: str = "mediana"
    antiguedad_max_meses: int = Field(default=6, ge=1)
    descuento_anuncio: float = Field(default=0.95, gt=0, le=1)
    margen_rango: float = Field(default=0.05, ge=0)
    iqr_k: float = Field(default=1.5, gt=0)
    planta_ascensor: PlantaAscensorCoef = Field(default_factory=PlantaAscensorCoef)
    estado: EstadoCoef = Field(default_factory=EstadoCoef)
    orientacion: OrientacionCoef = Field(default_factory=OrientacionCoef)
    extras: ExtrasCoef = Field(default_factory=ExtrasCoef)

    @field_validator("base_m2")
    @classmethod
    def _base(cls, v: str) -> str:
        if v not in {"construidos", "utiles"}:
            raise ValueError("base_m2 debe ser 'construidos' o 'utiles'")
        return v

    @field_validator("valor_central")
    @classmethod
    def _central(cls, v: str) -> str:
        if v not in {"mediana", "media"}:
            raise ValueError("valor_central debe ser 'mediana' o 'media'")
        return v
