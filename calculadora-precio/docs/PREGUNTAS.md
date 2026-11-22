# Preguntas abiertas (antes de programar)

## Coeficientes
1. ¿Qué valores para planta/ascensor, estado e exterior/interior? ¿Salen de tu experiencia, de datos de la agencia o de otra fuente?
2. ¿Terraza, garaje y trastero: valor fijo en € o porcentaje? ¿Qué importes en tu zona?
3. ¿Debe influir el año de construcción y/o el certificado energético? ¿Cómo?
4. ¿Coeficiente de descuento de anuncio a cierre? ¿Lo calibras con cierres reales?
5. ¿Los coeficientes cambian por barrio?

## Método
6. ¿€/m² sobre **construidos** o **útiles**? (Recomiendo una sola base, igual en vivienda y comparables.)
7. ¿Media o mediana como valor base?
8. ¿Descarte de extremos: IQR, recorte fijo (min y máx) o manual?
9. ¿Margen del rango fijo (±%) o según la dispersión de los comparables?
10. ¿"Misma zona" = mismo barrio, distrito o radio en metros?
11. ¿Antigüedad máxima de un comparable (meses) antes de avisar o excluir?
12. ¿Diferencia máxima de m² entre comparable y vivienda (p. ej. ±30 %)?

## Fuentes y datos
13. ¿De dónde sacarás los comparables (consulta manual de portales, datos internos de la agencia, escrituras…)? ¿Tienes acceso a precios de cierre?
14. ¿Guardar URLs de portales en ficheros locales es aceptable para ti? ¿Habrá datos personales de propietarios en los ficheros?
15. ¿Normalizar los comparables con coeficientes (propuesto) o solo filtrar los parecidos?

## Producto
16. ¿Formato de números en informes (1.234,56 €)?
17. ¿Streamlit o FastAPI? ¿Uso solo local o compartido con compañeros?
18. ¿El PDF debe llevar logo/marca RE/MAX? (Habría que revisar las normas de marca de la franquicia.)
19. ¿Texto legal del aviso "no es una tasación"? ¿Lo revisa la agencia?
20. ¿Gestor de entorno preferido (uv, pip+venv, poetry) y CI en GitHub Actions?
21. ¿El código vivirá en `calculadora-precio/` de este repo o en un repo propio?
