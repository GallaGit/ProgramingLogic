# Expresiones equilibradas

**Nivel:** Medio · **Estado:** Por hacer

## Enunciado

Dada una cadena con parentesis/corchetes/llaves, comprueba si estan
correctamente abiertos y cerrados en orden.

Ejemplos:
- `{ [ a * ( c + d ) ] - 5 }` → equilibrada
- `{ a * ( c + d ) ] - 5 }` → no
- `{ a * c + [ d - 5 ) }` → no

## Pistas

1. Piensa en una **pila** (stack): array con `push` / `pop`.
2. Si ves un simbolo de apertura → lo apilas.
3. Si ves uno de cierre → debe coincidir con el ultimo abierto.
4. Al final la pila debe quedar vacia.
5. Ignora el resto de caracteres (letras, numeros, operadores).

## Tu codigo

Escribe todo en `app.js`. Este reto entrena mucho la logica.
