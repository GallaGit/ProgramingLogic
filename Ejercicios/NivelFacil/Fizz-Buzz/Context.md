Hola! Es un excelente momento para poner a prueba tu lógica. El ejercicio Fizz-Buzz es un clásico en las entrevistas técnicas para perfiles Junior porque, aunque parece simple, revela si un programador entiende el orden de ejecución y las estructuras de control
.
Como tu mentor, no solo te daré el código; vamos a desglosarlo para que entiendas cómo piensa un programador al resolverlo.

--------------------------------------------------------------------------------
🟢 NIVEL BÁSICO: El problema y su lógica
Qué es: Un programa que recorre una lista de números y sustituye algunos por palabras basándose en su divisibilidad
.
Para qué sirve: Para practicar el uso de bucles (for), condicionales (if/elif/else) y el operador de residuo (%)
.
Cómo funciona: Se evalúa cada número: si es múltiplo de 3, de 5, o de ambos, se imprime un texto; si no, se imprime el número
.

--------------------------------------------------------------------------------
🧠 Análisis del Algoritmo (Pensamiento Computacional)
Antes de escribir una sola línea de código, debemos dividir el problema en pasos pequeños:
El Rango: Necesitamos movernos del número 1 al 100
.
La Condición Crítica: Aquí es donde muchos fallan. Si un número es múltiplo de 3 y de 5 (como el 15), el programa debe decir "FizzBuzz"
.
El Orden de Evaluación: Como el código se ejecuta de arriba hacia abajo, debemos comprobar primero la condición más difícil (ser múltiplo de ambos)
. Si comprobamos primero si es múltiplo de 3, el número 15 imprimiría "Fizz" y saltaría a la siguiente instrucción, ignorando que también era múltiplo de 5
.
Razonamiento antes del código:
¿Cómo sé si un número es múltiplo de otro? Usando el operador de módulo (%). Si numero % 3 == 0, el residuo es cero, por lo tanto, es múltiplo
.
Pseudocódigo:
PARA cada número del 1 al 100:
    SI número es múltiplo de 3 Y de 5: IMPRIMIR "FizzBuzz"
    SINO SI número es múltiplo de 3: IMPRIMIR "Fizz"
    SINO SI número es múltiplo de 5: IMPRIMIR "Buzz"
    SINO: IMPRIMIR el número

--------------------------------------------------------------------------------
💻 Implementación en Código (Python)
Siguiendo la lógica de las fuentes, aquí tienes el código explicado línea por línea
:
def fizz_buzz(text1, text2):
    # Creamos un rango del 1 al 100 (el 101 es excluido) [3]
    for number in range(1, 101):
        
        # 1. Comprobamos la condición más restrictiva primero [1, 4]
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2) # Concatena "Fizz" y "Buzz" [1]
            
        # 2. Si no es múltiplo de ambos, probamos si es solo de 3 [2]
        elif number % 3 == 0:
            print(text1)
            
        # 3. Si no es de 3, probamos con el 5 [4]
        elif number % 5 == 0:
            print(text2)
            
        # 4. Si no cumple nada de lo anterior, imprimimos el número [2]
        else:
            print(number)

# Llamada a la función con los textos clásicos
fizz_buzz("Fizz", "Buzz")

--------------------------------------------------------------------------------
⚠️ Error Común: El Orden de los Factores
El error más frecuente es poner la condición de number % 3 == 0 al principio del bloque if
. Si haces esto, cuando el programa llegue al número 15, verá que es divisible por 3, imprimirá "Fizz" y pasará al número 16
. Nunca llegará a evaluar si era divisible por 5
.
🛠️ Cómo se usa en proyectos reales
Esta lógica de "filtrado por prioridades" se usa, por ejemplo, en sistemas de categorización de facturas o en validaciones de seguridad (donde primero compruebas si el usuario es administrador ANTES de comprobar si es un usuario normal).

--------------------------------------------------------------------------------
🏁 Mini Retos y Preguntas "Junior"
Pregunta de entrevista: "¿Por qué usamos elif en lugar de varios if independientes en este ejercicio?"
Respuesta sugerida: Porque queremos que solo se ejecute una de las opciones por cada número. Si usáramos varios if, el número 15 imprimiría "FizzBuzz", luego "Fizz" y luego "Buzz" por separado.
Reto de lógica (Extra): Modifica la función para que, al final, te diga cuántos números se imprimieron en total (sin contar los que fueron sustituidos por texto)
.
Pista: Necesitas un contador que empiece en 0 e incremente solo dentro del bloque else
.
¿Qué parte del orden de prioridad te resultó más curiosa? Si quieres, podemos intentar añadirle más condiciones, como un "FizzBuzzWoof" para múltiplos de 7.