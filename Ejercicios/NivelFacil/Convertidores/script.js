/*
formulas de conversion de temperatura
F = (C × 9/5) + 32
C = (F - 32) × 5/9
*/

const inputTemp = document.getElementById("convTemperatura");
const convType = document.getElementById("convType");
const convBtn = document.getElementById("convertir");
const convResult = document.getElementById("resultado");


convBtn.addEventListener("click", () => {
    //const temp = inputTemp.value;
    const conv = convType.value;
    const tempNumber = Number(inputTemp.value);

    if (isNaN(tempNumber)) {
    console.log("Error. Escribe un numero por favor")
} else {
      //falta la formulas si estan en la opcion C-F y F-C
      if (conv === "CtoF") {
        //formula C - F
        convResult.textContent = `${(tempNumber * 9/5) + 32}`;
      } else {
        //Formula F to C
        convResult.textContent = `${(tempNumber - 32) * 5/9}`;
      }
}

});


//Formulas de conversion de distancia
// 1 metro = 0.001 kilometros
// 1 kilometro = 1000 metros


