<div align="center">

# Fizz Buzz

### Ejercicio clasico de logica de programacion

[![Status](https://img.shields.io/badge/Estado-En%20Progreso-yellow)]()
[![JavaScript](https://img.shields.io/badge/Lenguaje-JavaScript-F7DF1E?logo=javascript&logoColor=black)]()

</div>

---

## Descripcion

Programa que recorre los numeros del 1 al 100 y:

| Condicion | Resultado |
|-----------|-----------|
| Multiplo de 3 **y** 5 | `FizzBuzz` |
| Multiplo de 3 | `Fizz` |
| Multiplo de 5 | `Buzz` |
| Ninguno | El numero |

---

## Errores que cometi

> [!WARNING]
> - No leer bien el contexto del problema
> - No plantear un pseudocodigo antes de escribir codigo
> - Mala estructura del `for` loop
> - Confundir `&&` (Y) con `||` (O), lo que causaba que "FizzBuzz" se imprimiera en cada multiplo de 3 o 5 por separado

---

## Lo que aprendi

> [!TIP]
> - El **orden de evaluacion** importa: la condicion mas restrictiva (`% 3 && % 5`) debe ir **primero**
> - Usar `elif` / `else if` en lugar de multiples `if` independientes para que solo se ejecute **una** rama por numero
> - El operador modulo `%` devuelve el residuo de una division — si es `0`, el numero es multiplo

---

## Objetivos

- [x] Resolver el ejercicio FizzBuzz en consola
- [ ] Llevar el ejercicio al navegador (HTML + CSS + JS)

---

## Ejecucion

```bash
node script.js
```

---

<div align="center">

*Consulta el archivo [`Context.md`](Context.md) para ver la guia completa del ejercicio.*

</div>
