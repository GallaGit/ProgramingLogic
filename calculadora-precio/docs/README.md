# Calculadora de precio de venta por comparables

## Qué hace
Estima un **rango de precio de venta** (mínimo, recomendado, máximo) de una vivienda a partir de entre 3 y 10 comparables de la misma zona que introduce el usuario, aplicando coeficientes de ajuste configurables.

## Para quién es
Agentes inmobiliarios (uso inicial: RE/MAX Sorolla, Valencia) que necesitan preparar una valoración orientativa **antes de visitar al propietario**.

## Qué NO hace
- **No es una tasación oficial** (no sustituye a una tasación homologada ni a un tasador).
- **No sustituye la visita**: estado real, orientación, ruido, cargas, etc. solo se valoran en persona.
- **No obtiene datos de portales**: no hace scraping de Idealista ni Fotocasa (sus condiciones lo prohíben y bloquean bots). Los comparables se introducen a mano o por CSV.
- **No trae datos de mercado propios**: los coeficientes son parámetros que define el agente; los valores por defecto son solo ejemplo.
- No garantiza un precio de cierre: los precios de anuncio no son precios de venta.

## Documentación
| Documento | Contenido |
|---|---|
| [LOGICA.md](LOGICA.md) | Método de cálculo paso a paso |
| [DATOS.md](DATOS.md) | Modelo de datos y formato CSV |
| [ARQUITECTURA.md](ARQUITECTURA.md) | Stack, carpetas y tests |
| [ROADMAP.md](ROADMAP.md) | Iteraciones previstas |
| [PREGUNTAS.md](PREGUNTAS.md) | Decisiones pendientes |

## Estado
Iteración 1: solo documentación. Sin código.
