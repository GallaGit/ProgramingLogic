/*
formulas de conversion de temperatura
F = (C × 9/5) + 32
C = (F - 32) × 5/9
*/

const inputUni = document.getElementById("convUniv");
const convType = document.getElementById("convType");
const convBtn = document.getElementById("convertir");
const convResult = document.getElementById("resultado");


convBtn.addEventListener("click", () => {
    const conv = convType.value;
    const uniNumber = Number(inputUni.value);

    if (isNaN(uniNumber)) {
      convResult.textContent = "Error. Escribe un numero valido por favor.";
      return;
    }

    let result;

    switch (conv) {
      case "CtoF":
        result = (uniNumber * 9 / 5) + 32;
        convResult.textContent = `${uniNumber} °C = ${result.toFixed(2)} °F`;
        break;
      case "FtoC":
        result = (uniNumber - 32) * 5 / 9;
        convResult.textContent = `${uniNumber} °F = ${result.toFixed(2)} °C`;
        break;
      case "Kg":
        result = uniNumber * 2.20462;
        convResult.textContent = `${uniNumber} kg = ${result.toFixed(2)} lb`;
        break;
      case "Lb":
        result = uniNumber / 2.20462;
        convResult.textContent = `${uniNumber} lb = ${result.toFixed(2)} kg`;
        break;
      case "MtoKm":
        result = uniNumber / 1000;
        convResult.textContent = `${uniNumber} m = ${result.toFixed(3)} km`;
        break;
      case "KmtoM":
        result = uniNumber * 1000;
        convResult.textContent = `${uniNumber} km = ${result.toFixed(2)} m`;
        break;
      default:
        convResult.textContent = "Selecciona un tipo de conversion valido.";
    }

});


//Formulas de conversion de distancia
// 1 metro = 0.001 kilometros
// 1 kilometro = 1000 metros


