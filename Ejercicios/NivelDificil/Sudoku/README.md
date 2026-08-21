# Sudoku (validador / solver basico)

**Nivel:** Dificil · **Estado:** Por hacer

## Enunciado (elige una variante)

**Variante A (recomendada primero):** Validar un tablero 9x9:
¿cumple las reglas de filas, columnas y bloques 3x3?

**Variante B (extra):** Resolver un sudoku incompleto (backtracking).

## Pistas

1. Representa el tablero como matriz 9x9 (`0` = vacio).
2. Para validar: en cada fila/columna/bloque, no debe haber duplicados (salvo 0).
3. Sets o arrays de “vistos” ayudan a detectar repeticiones.
4. Si vas a resolver: prueba un numero 1–9, avanza, y si falla… deshaz (backtracking).
5. No hace falta UI perfecta al principio: `console.log` del tablero basta.

## Tu codigo

Empieza por la variante A. La B cuando A te quede clara.
