# Calculadora de precio por comparables

Estimación orientativa del precio de venta de una vivienda a partir de 3–10 comparables de la misma zona. Pensada para agentes (p. ej. RE/MAX Sorolla, Valencia) que preparan valoraciones **antes de la visita**.

**No es una tasación oficial.** No sustituye la visita. No hace scraping de Idealista ni Fotocasa.

Documentación de diseño: [`docs/`](docs/).

## Requisitos

- Python 3.12+

## Instalación

```bash
cd calculadora-precio
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Los coeficientes viven en `config/coeficientes.example.toml` (todos marcados **EJEMPLO, AJUSTAR**). Para personalizar:

```bash
cp config/coeficientes.example.toml config/coeficientes.toml
# edita coeficientes.toml y pásalo con --config
```

## CLI

```bash
calculadora-precio estimar \
  --csv examples/comparables_ejemplo.csv \
  --direccion "Calle Ejemplo 1" \
  --barrio "BarrioEjemplo" \
  --m2-construidos 90 \
  --m2-utiles 75 \
  --habitaciones 3 \
  --banos 2 \
  --planta 3 \
  --ascensor \
  --estado buen_estado \
  --orientacion exterior \
  --fecha-ref 2026-11-28
```

Opcional: `--config ruta.toml`, `--json salida.json`.

## Interfaz web (Streamlit)

```bash
streamlit run src/calculadora_precio/web/app.py
```

Introduce la vivienda y los comparables (manual o CSV) y verás el rango mínimo / recomendado / máximo y la explicación de ajustes.

## Tests

```bash
pytest
```

## Decisiones por defecto (revisables)

Ver [`docs/PREGUNTAS.md`](docs/PREGUNTAS.md): m² construidos, mediana como valor central, IQR solo con ≥5 comparables, misma zona = mismo barrio, antigüedad máx. 6 meses.

## CSV de ejemplo

`examples/comparables_ejemplo.csv` — **datos inventados**, no reales.

## Aviso

Los precios de anuncio no son precios de cierre. La herramienta aplica un descuento configurable (EJEMPLO, AJUSTAR) a los anuncios.
