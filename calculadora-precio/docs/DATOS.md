# Modelo de datos

Validación con pydantic (ver [ARQUITECTURA.md](ARQUITECTURA.md)). Campos en español, sin tildes, `snake_case`.

## Vivienda
| Campo | Tipo | Obligatorio | Notas |
|---|---|---|---|
| direccion | texto | sí | |
| barrio | texto | sí | Define la zona |
| m2_construidos | decimal > 0 | sí | |
| m2_utiles | decimal > 0 | sí | ≤ m2_construidos |
| habitaciones | entero ≥ 0 | sí | |
| banos | entero ≥ 0 | sí | |
| planta | entero (0 = bajo) | sí | |
| ascensor | bool | sí | |
| estado | `a_reformar` \| `buen_estado` \| `reformado` | sí | |
| orientacion | `exterior` \| `interior` | sí | |
| terraza | bool (+ `m2_terraza` opcional) | sí | |
| garaje | bool | sí | |
| trastero | bool | sí | |
| anio_construccion | entero | no | |
| certificado_energetico | A–G \| `en_tramite` \| `desconocido` | no | |

## Comparable
| Campo | Tipo | Obligatorio | Notas |
|---|---|---|---|
| precio | decimal > 0 (€) | sí | |
| m2 | decimal > 0 | sí | Misma base (construidos/útiles) que la vivienda |
| eur_m2 | calculado | — | precio / m2 |
| tipo_precio | `anuncio` \| `cierre` | sí | |
| fuente | texto | sí | p. ej. "Consulta manual de portal", "Escritura", "Agencia" |
| url | URL | no | Enlace de referencia |
| fecha | fecha ISO | sí | Fecha del anuncio/cierre |
| barrio | texto | sí | |
| planta, ascensor, estado, orientacion | como en vivienda | sí | Para normalizar |
| terraza, garaje, trastero | bool | no | |
| notas | texto | no | |

Reglas: 3 ≤ nº comparables ≤ 10; sin duplicados (misma URL o mismo precio+m²+barrio); aviso si la fecha supera N meses (parámetro, ver PREGUNTAS).

## Resultado
| Campo | Descripción |
|---|---|
| precio_minimo, precio_recomendado, precio_maximo | € |
| eur_m2_medio, eur_m2_mediana | tras normalizar y descartar |
| comparables_usados / descartados | con motivo del descarte |
| coeficientes_aplicados | copia de la configuración usada |
| n_anuncio, n_cierre | recuento por tipo de precio |
| avisos | lista de textos (pocos comparables, dispersión, antigüedad…) |
| fecha_calculo | marca temporal |

## CSV de entrada (comparables)
UTF-8, separador `,`, decimales con punto, cabecera obligatoria, booleanos `si`/`no`, fechas `AAAA-MM-DD`. Una fila por comparable.

> **EJEMPLO INVENTADO. Datos ficticios, no reales.**

```csv
precio,m2,tipo_precio,fuente,url,fecha,barrio,planta,ascensor,estado,orientacion,terraza,garaje,trastero,notas
100000,50,anuncio,Manual,https://example.com/a,2026-01-15,BarrioEjemplo,2,si,buen_estado,exterior,no,no,no,EJEMPLO ficticio
120000,60,cierre,Agencia,,2026-02-01,BarrioEjemplo,0,no,a_reformar,interior,no,no,si,EJEMPLO ficticio
150000,70,anuncio,Manual,https://example.com/c,2026-02-10,BarrioEjemplo,5,si,reformado,exterior,si,si,no,EJEMPLO ficticio
```
