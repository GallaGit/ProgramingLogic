# Preguntas y decisiones

## Decidido por defecto (revisable)

| # | Tema | Decisión |
|---|---|---|
| 6 | Base €/m² | **m² construidos** (misma base en vivienda y comparables). |
| 7 | Valor central | **Mediana** como valor base; la media solo es informativa. |
| 8 | Extremos | **IQR** solo con **≥ 5** comparables; con menos no se descarta. |
| 10 | Misma zona | **Mismo barrio** que indica el usuario (comparación normalizada, sin mayúsculas). |
| 11 | Antigüedad | Máximo **6 meses** (configurable en TOML); más antiguos se excluyen. |
| 4 | Anuncio → cierre | Multiplicador **configurable** en TOML; valor por defecto marcado **EJEMPLO, AJUSTAR**. |
| — | Coeficientes | Todos en `config/coeficientes.example.toml`, marcados **EJEMPLO, AJUSTAR**. |
| 9 | Margen del rango | Fijo ±% en TOML (**EJEMPLO, AJUSTAR**). |
| 17 | Interfaz | **Streamlit** (iteración 4). |
| 21 | Ubicación | `calculadora-precio/` en este repo. |

## Sigue abierto / revisable

### Coeficientes
1. Valores reales de planta/ascensor, estado e exterior/interior (hoy solo EJEMPLO).
2. Terraza, garaje y trastero: importes reales en tu zona (hoy 0 €).
3. ¿Debe influir año de construcción y/o certificado energético? (hoy no ajustan).
5. ¿Coeficientes distintos por barrio?

### Método
12. ¿Diferencia máxima de m² entre comparable y vivienda?

### Fuentes y datos
13. Fuentes habituales de comparables y acceso a precios de cierre.
14. Política de URLs y datos personales en ficheros locales.
15. Confirmar normalización por coeficientes (implementada) vs. solo filtrar parecidos.

### Producto
16. Formato de números en informes (1.234,56 €).
18. Logo/marca RE/MAX en el PDF (iteración 5).
19. Texto legal del aviso "no es una tasación".
20. Gestor de entorno preferido y CI en GitHub Actions.
