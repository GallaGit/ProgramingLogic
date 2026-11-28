# Arquitectura propuesta

## Stack
- **Python 3.12**
- **pydantic v2**: validación de vivienda, comparables y configuración.
- **pandas**: cálculos (€/m², cuartiles, media/mediana).
- **Typer**: CLI.
- **Streamlit o FastAPI** (más adelante): interfaz web. Recomendación: Streamlit (un solo usuario, rápido de construir); FastAPI solo si hace falta API.
- **pytest**: tests. Opcional: `ruff` (lint/formato).
- Informe PDF (iteración 5): librería por decidir.

## Estructura de carpetas
```
calculadora-precio/
├── docs/                    # esta documentación
├── pyproject.toml
├── config/
│   └── coeficientes.example.toml   # valores EJEMPLO, AJUSTAR
├── src/calculadora_precio/
│   ├── modelos.py           # Vivienda, Comparable, Resultado, Config (pydantic)
│   ├── configuracion.py     # carga/validación de coeficientes
│   ├── comparables.py       # lectura CSV, validación, normalización
│   ├── calculo.py           # extremos, estadísticos, rango (sin I/O)
│   ├── avisos.py            # reglas de avisos
│   ├── cli.py               # Typer
│   └── web/                 # iteración 4
├── tests/
│   ├── test_modelos.py
│   ├── test_comparables.py
│   ├── test_calculo.py
│   ├── test_cli.py
│   └── data/                # CSV ficticios de prueba
└── README.md
```

## Principios
- **Núcleo puro**: `calculo.py` no hace I/O; recibe modelos y configuración y devuelve `Resultado`. Reutilizable en CLI y web.
- **Coeficientes fuera del código** (TOML), validados con pydantic.
- **Sin red**: ninguna llamada a portales.
- Datos reales de propietarios/clientes no se versionan (`.gitignore`).

## Tests (pytest)
- Validación: <3 y >10 comparables, m² ≤ 0, útiles > construidos, duplicados.
- Cálculo con casos pequeños verificables a mano, con datos ficticios.
- Extremos: con y sin atípicos; <5 comparables no descarta.
- Coeficientes: todos 1,00 ⇒ sin ajuste; cambiar un parámetro ⇒ cambio esperado.
- Anuncio vs. cierre.
- CLI con `typer.testing.CliRunner`.
- CI (GitHub Actions) con pytest: por decidir.
