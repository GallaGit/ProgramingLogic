Te lo dejo en formato **README / LEARNED.md** listo para copiar y pegar:

````md
# 📚 Lesson Learned - Generador de Contraseñas + TypeScript

## 🎯 Objetivo del proyecto

Crear un generador de contraseñas usando TypeScript, manipulando el DOM, eventos y lógica básica de programación.

El usuario puede:
- Introducir la longitud deseada.
- Presionar un botón.
- Generar una contraseña aleatoria.
- Mostrar el resultado en pantalla.

---

# 1. Conceptos principales aprendidos

## Manipulación del DOM con TypeScript

Para acceder a elementos HTML usamos:

```ts
document.getElementById()
````

Ejemplo:

```ts
const result = document.getElementById("result") as HTMLParagraphElement;
```

TypeScript no sabe qué tipo de elemento devuelve `getElementById`, por eso usamos:

```ts
as HTMLInputElement
as HTMLButtonElement
as HTMLParagraphElement
```

Esto se llama **type assertion**.

Significa:

> "Sé que este elemento HTML es de este tipo, trátalo como tal".

---

# 2. Diferencia entre value y textContent

## Inputs

Los elementos como:

```html
<input>
```

usan:

```ts
.value
```

Ejemplo:

```ts
const input = document.getElementById("length") as HTMLInputElement;

input.value;
```

Siempre devuelve un `string`.

Ejemplo:

```ts
"8"
```

No:

```ts
8
```

---

## Elementos de texto

Elementos como:

```html
<p>
<h1>
<div>
<span>
```

usan:

```ts
.textContent
```

Ejemplo:

```ts
result.textContent = password;
```

---

# 3. Conversión de tipos

Como `.value` devuelve string:

```ts
const value = input.value;
```

tenemos:

```ts
"10"
```

Para convertirlo a número:

```ts
const number = Number(value);
```

Resultado:

```ts
10
```

---

# 4. Generación aleatoria de caracteres

Creamos una cadena con todos los caracteres posibles:

```ts
const chars: string =
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
```

Obtenemos un índice aleatorio:

```ts
const randomIndex =
Math.floor(Math.random() * chars.length);
```

Proceso:

`Math.random()`

genera un decimal:

```
0.453
```

Multiplicamos por la longitud:

```
0.453 * 62
```

Resultado:

```
28.086
```

`Math.floor()` elimina los decimales:

```
28
```

Ese número sirve como posición:

```ts
chars[28]
```

Obtiene un carácter.

---

# 5. Construcción de strings

Creamos una contraseña vacía:

```ts
let password: string = "";
```

Cada iteración añadimos un carácter:

```ts
password += randomChar;
```

Ejemplo:

Inicial:

```
""
```

Primera vuelta:

```
"A"
```

Segunda:

```
"A7"
```

Tercera:

```
"A7k"
```

---

# 6. Uso del bucle for

Como sabemos cuántas veces repetir:

```ts
for(let i = 0; i < passLength; i++)
```

es mejor que usar `while`.

Ejemplo:

Si:

```ts
passLength = 8
```

el bucle genera 8 caracteres.

---

# 7. Eventos del usuario

El error inicial fue ejecutar la lógica al cargar la página.

Problema:

El usuario todavía no había escrito la longitud.

Solución:

Usar eventos:

```ts
button.addEventListener("click", () => {

});
```

Ahora el código solo funciona cuando el usuario hace click.

---

# 8. Error con variable length

No usar:

```ts
length
```

porque existe como propiedad global de JavaScript.

Puede causar:

```
Cannot redeclare 'length'
```

Mejor:

```ts
passLength
passwordLength
```

---

# 9. Configuración TypeScript

TypeScript ya estaba instalado en:

```json
package.json
```

Creamos:

```
tsconfig.json
```

para controlar la compilación.

---

## Scripts utilizados

Compilar todos los ejercicios:

```bash
npm run build
```

Modo observación:

```bash
npm run build:watch
```

Compilar solo el generador:

```bash
npm run build:password
```

Modo watch del generador:

```bash
npm run build:password:watch
```

---

# 10. Errores de compilación encontrados

## TS5112

Problema:

```bash
tsc archivo.ts
```

con `tsconfig.json`.

Solución:

```bash
npx tsc
```

o:

```bash
tsc -p carpeta
```

---

## TS5058

La ruta del proyecto no coincidía con la carpeta actual.

Solución:

Desde la raíz:

```bash
npx tsc -p Ejercicios/NivelMedio/GeneradorDeContraseñas
```

Dentro del ejercicio:

```bash
npx tsc
```

---

# 11. Flujo de trabajo aprendido

1. Editar:

```
app.ts
```

2. Guardar cambios.

3. Compilar:

```bash
npm run build:password
```

4. Abrir:

```
index.html
```

5. Probar la aplicación.

---

# Estado final del proyecto

HTML:

* Input:

```
#length
```

* Botón:

```
#generate
```

* Resultado:

```
#result
```

TypeScript:

* Lee longitud.
* Genera caracteres aleatorios.
* Construye la contraseña.
* Actualiza el DOM.

---

# Ideas para mejorar en futuras versiones

* Crear una función generatePassword().
* Añadir opciones:

  * Mayúsculas.
  * Números.
  * Símbolos.
* Botón copiar contraseña.
* Mostrar nivel de seguridad.
* Evitar caracteres repetidos.

---

## Conocimientos practicados

✅ Variables
✅ Strings
✅ Number conversion
✅ Loops
✅ Math.random()
✅ Math.floor()
✅ DOM
✅ Eventos
✅ TypeScript types
✅ Type assertions
✅ Compilación TS → JS

```

Este desafío ya te dejó varias bases que vas a reutilizar muchísimo en React: **estado, eventos, inputs, tipos y actualización de UI**.
```
