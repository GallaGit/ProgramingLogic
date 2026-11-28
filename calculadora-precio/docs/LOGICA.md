# Lógica de cálculo

> Todos los porcentajes de este documento son **EJEMPLO, AJUSTAR**. No son datos de mercado.

## 1. Entrada: la vivienda a valorar
Dirección y barrio, m² construidos, m² útiles, habitaciones, baños, planta, ascensor (sí/no), estado (`a_reformar` / `buen_estado` / `reformado`), exterior/interior, terraza (sí/no, opcional m²), garaje, trastero, año de construcción, certificado energético (A–G o "en trámite"/desconocido). Detalle de campos en [DATOS.md](DATOS.md).

## 2. Comparables
- Mínimo **3**, máximo **10**, de la **misma zona** (= **mismo barrio**; decidido por defecto, revisable).
- Cada uno: precio, m², €/m² (calculado), fuente, URL, fecha, y si es precio de anuncio o de cierre.
- Entrada manual o CSV. **Sin scraping** de Idealista/Fotocasa.
- Cada comparable también lleva sus características (planta, ascensor, estado, exterior, extras) para poder **normalizarlo**.
- Menos de 3 o más de 10 → error de validación claro.

## 3. Pasos del cálculo
1. **Validar** entrada y comparables.
2. **Precio de referencia por comparable**: €/m² = precio / m² (**base = construidos** por defecto; misma base en vivienda y comparables).
3. Filtrar por **barrio** y **antigüedad** (máx. 6 meses por defecto, configurable).
4. **Marcar anuncio vs. cierre** (sección 5) y aplicar el descuento de negociación a los de anuncio.
5. **Normalizar cada comparable** a las características de la vivienda: cociente entre coeficientes vivienda/comparable (planta/ascensor, estado, exterior).
6. **Descartar extremos** (IQR) solo con **≥ 5** comparables. Con menos no se descarta. Siempre se informa qué se descartó.
7. **Estadísticos**: mediana = valor base; media solo informativa.
8. **Valor base de la vivienda** = €/m² mediana × m² construidos.
9. **Extras** (terraza, garaje, trastero) como suma fija (parámetro; por defecto 0).
10. **Rango** con margen fijo ±% (EJEMPLO, AJUSTAR):
   - recomendado = valor base + extras
   - mínimo = recomendado × (1 − margen)
   - máximo = recomendado × (1 + margen)
11. **Resultado** con: rango, €/m² usados, comparables incluidos/descartados, explicación de ajustes, coeficientes aplicados y avisos.

## 4. Coeficientes (parámetros configurables)
Se guardan en un fichero de configuración (`toml`), no en el código. Multiplicadores sobre el €/m²; 1,00 = sin ajuste.

| Factor | Opción | Valor | Estado |
|---|---|---|---|
| Planta/ascensor | Bajo sin ascensor | 0,95 | EJEMPLO, AJUSTAR |
| | Intermedia con ascensor | 1,00 | EJEMPLO, AJUSTAR |
| | Alta con ascensor | 1,03 | EJEMPLO, AJUSTAR |
| | 3.ª o superior sin ascensor | 0,93 | EJEMPLO, AJUSTAR |
| Estado | a reformar | 0,85 | EJEMPLO, AJUSTAR |
| | buen estado | 1,00 | EJEMPLO, AJUSTAR |
| | reformado | 1,08 | EJEMPLO, AJUSTAR |
| Orientación | exterior | 1,00 | EJEMPLO, AJUSTAR |
| | interior | 0,92 | EJEMPLO, AJUSTAR |
| Terraza | por m² o % | 0,00 | EJEMPLO, AJUSTAR |
| Garaje | valor fijo € | 0 | EJEMPLO, AJUSTAR |
| Trastero | valor fijo € | 0 | EJEMPLO, AJUSTAR |
| Descuento anuncio → cierre | multiplicador | 0,95 | EJEMPLO, AJUSTAR |
| Margen del rango | ± % | 0,05 | EJEMPLO, AJUSTAR |
| Factor IQR (extremos) | k | 1,5 | EJEMPLO, AJUSTAR |

Año de construcción y certificado energético: se registran y se muestran en el informe; **no ajustan el precio** hasta que el agente defina coeficientes (ver PREGUNTAS). Los extras valen 0 por defecto a propósito, para no inventar importes.

## 5. Precio de anuncio vs. precio de cierre
Los precios de anuncio **no** son precios de cierre. Marcado:
- Campo obligatorio `tipo_precio` en cada comparable: `anuncio` o `cierre`.
- Los `cierre` (p. ej. de escritura o dato interno de la agencia) se usan tal cual.
- Los `anuncio` se multiplican por el coeficiente "descuento anuncio → cierre" (EJEMPLO, AJUSTAR; el agente lo calibra con su experiencia o con cierres reales).
- El resultado indica cuántos comparables son de cada tipo y avisa si todos son de anuncio.
- Opcional: campo `precio_rebajado_desde` para anotar rebajas observadas.

## 6. Límites
Con pocos comparables o alta dispersión el rango es poco fiable; el informe lo dice. Este método es orientativo y no sustituye a una tasación ni a la visita.
