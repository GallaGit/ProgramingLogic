/*aca capturo los botones y el display(input) */
const display = document.getElementById("display");
const addNumbers = document.querySelectorAll(".number-btn");
const addOperators = document.querySelectorAll(".operator-btn");
const result = document.querySelector(".equals-btn")
const clear = document.querySelector(".clear-btn")


let firstNumber = ("");
let operator = ("");
let secondNumber = ("");
/*
LOGICA DE LOS NUMEROS
1. Guardar botones en una variable
2. Recorrer botones
3. Escuchar clicks
4. Obtener texto del botón
5. Mostrarlo en el input 
*/

addNumbers.forEach(number => {
    number.addEventListener("click", () => {
        display.value += number.textContent;
    })
})

/*LOGICA DE LOS OPERADORES*/


if (operator === false) {
    display.value += firstNumber
} else if (operator) {
    display.value += secondNumber
}

addOperators.forEach(operators => {
    operators.addEventListener("click", () => {
        operator = operators.textContent;
    })

})

clear.addEventListener("click", () => {
    display.value = ("");
})
