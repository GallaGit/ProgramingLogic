"use strict";
const userInput = "5";
const expectedValue = 5;
const userInputNumber = Number(userInput);
// Evita la igualdad débil — esto devuelve true debido a la coerción de tipos
/*if (userInput == expectedValue) {
  console.log("Igualdad débil coincidió (evita esto)");
}*/
// Usa igualdad estricta — verifica tipo y valor
if (userInputNumber === expectedValue) {
    console.log("Igualdad estricta coincidió (correcto)");
}
else {
    console.log("Igualdad estricta no coincidió (esperado)");
}
