# 🧮 Calculadora Básica con JavaScript

## 📌 Descripción

Proyecto realizado como práctica de lógica de programación, manipulación del DOM y eventos en JavaScript.

El objetivo fue construir una calculadora funcional desde cero sin utilizar `eval()`, entendiendo cada paso de la lógica en lugar de copiar una solución completa.

---

# 🎯 Objetivos de Aprendizaje

Durante este desafío se practicaron los siguientes conceptos:

* Selección de elementos del DOM.
* Eventos de usuario (`click`).
* Uso de `forEach()`.
* Funciones flecha (`=>`).
* Manipulación de inputs mediante `.value`.
* Obtención de texto mediante `.textContent`.
* Variables de estado.
* Conversión de tipos de datos.
* Operadores matemáticos.
* Depuración de errores.
* Diferencia entre asignación y comparación.

---

# 📚 Conceptos Aprendidos

## 1. Selección de elementos

### Capturar un elemento

```js
const display = document.getElementById("display");
```

### Capturar múltiples elementos

```js
const buttons = document.querySelectorAll(".number-btn");
```

---

## 2. Recorrer elementos

Para ejecutar una acción sobre cada botón:

```js
buttons.forEach(button => {
    // lógica
});
```

---

## 3. Eventos

Escuchar cuando el usuario hace click:

```js
button.addEventListener("click", () => {
    // acción
});
```

---

## 4. Obtener texto de un botón

```js
button.textContent
```

Ejemplo:

```html
<button>7</button>
```

Resultado:

```txt
7
```

---

## 5. Mostrar información en un input

Los inputs utilizan:

```js
display.value
```

No utilizan:

```js
display.innerText
```

---

## 6. Operador +=

Permite agregar contenido al existente.

```js
display.value += number.textContent;
```

Ejemplo:

```txt
Click 1 → 1
Click 2 → 12
Click 3 → 123
```

---

## 7. Variables de Estado

La calculadora necesita recordar información entre eventos.

```js
let firstNumber = "";
let operator = "";
let secondNumber = "";
```

Estas variables funcionan como la memoria de la calculadora.

---

## 8. Flujo de una operación

Ejemplo:

```txt
12 + 5 =
```

Estado interno:

```js
firstNumber = "12";
operator = "+";
secondNumber = "5";
```

---

## 9. Conversión de Strings a Números

Los inputs siempre devuelven texto.

```js
display.value
```

Devuelve:

```txt
"12"
```

Para calcular:

```js
Number("12")
```

Resultado:

```txt
12
```

---

## 10. Comparaciones

### Asignación

```js
=
```

Ejemplo:

```js
x = 5;
```

---

### Comparación débil

```js
==
```

Ejemplo:

```js
"5" == 5
```

Resultado:

```txt
true
```

---

### Comparación estricta

```js
===
```

Ejemplo:

```js
"5" === 5
```

Resultado:

```txt
false
```

Recomendación:

```txt
Usar siempre ===
```

---

# 🐛 Errores Encontrados y Corregidos

## Error: querySelectorALL

Incorrecto:

```js
querySelectorALL()
```

Correcto:

```js
querySelectorAll()
```

---

## Error: number()

Incorrecto:

```js
number("12")
```

Correcto:

```js
Number("12")
```

---

## Error: operador de asignación

Incorrecto:

```js
if (operator = "+")
```

Correcto:

```js
if (operator === "+")
```

---

## Error: reutilizar variables

Incorrecto:

```js
const result = document.querySelector(...)
result = num1 + num2;
```

Solución:

```js
let resultValue = 0;
```

---

# 🧠 Lección Más Importante

La calculadora ayudó a comprender que la mayoría de aplicaciones JavaScript siguen este patrón:

```txt
Evento → Estado → Acción
```

Ejemplos:

* Formularios
* Calculadoras
* Videojuegos
* React
* Angular
* Vue
* Aplicaciones Web

---

# 🚀 Próximos Proyectos Recomendados

1. Contador (+ / -)
2. Conversor de Temperaturas
3. Generador de Contraseñas
4. Piedra, Papel o Tijera
5. To Do List
6. Cronómetro
7. Adivina el Número
8. Tres en Raya

---

## Estado del Proyecto

✅ Calculadora funcional completada

Fecha: Junio 2026
