/*aca capturo los botones y el display(input) */
const display = document.getElementById("display");
const addNumbers = document.querySelectorAll(".number-btn");
const addOperators = document.querySelectorAll(".operator-btn");
const result = document.querySelector(".equals-btn")
const clear = document.querySelector(".clear-btn")

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
/*let firstNumber = ("");
let operator = ("");
let secondNumber = ("");

        if (firstNumber) {
            return firstNumber;
        } else if (operator) {
            return secondNumber;
        }
addOperators.forEach(operator => {
    operator.addEventListener("click", () => {
       
        display.value  
    })
})*/

clear.addEventListener("click", () => {
    display.value = ("");
});
