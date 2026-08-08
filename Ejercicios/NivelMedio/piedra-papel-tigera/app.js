const piedraBtn = document.getElementById("piedra");
const papelBtn = document.getElementById("papel");
const tijeraBtn = document.getElementById("tijera");

/*posibles resultados:*/
const options = [
    "🪨 Piedra",
    "📄 Papel",
    "✂️ Tijera"
    ];

let result = "";

/*Pseudo
1- Click en uno de los 3 botones
2- automaticamente se debe mostrar un random result
3- condiciones las del uego
4 mostrar en pantalla result y y tres estados victoria, derrota o empate
*/
/*const selection = ["🪨 Piedra" , "📄 Papel" , "✂️ Tijera"]

//jugador
const playerSelection = "🪨 Piedra";

//PC
button.addEventListener("click", () => {
    const randomSelection = Math.floor(Math.random() * selection.length);
    console.log(playerSelection);
    console.log(randomSelection);
})*/

/*Flujo
Jugador pulsa un botón
        ↓
Guardamos su elección
        ↓
La computadora elige aleatoriamente
        ↓
Comparamos las dos elecciones
        ↓
Ganaste / Perdiste / Empate
        ↓
Mostramos el resultado
*/

piedraBtn.addEventListener("click", () => {
    const playerOption = "🪨 Piedra";

    // Generamos un índice aleatorio
    const randomIndex = Math.floor(
        Math.random() * options.length
    );

    // Obtenemos la opción de la computadora
    const computerOption = options[randomIndex];

    console.log("Jugador:", playerOption);
    console.log("PC:", computerOption);

    // Determinamos el resultado
    if (playerOption === computerOption) {
        result = "Empate";
    } else if (
        playerOption === "🪨 Piedra" &&
        computerOption === "📄 Papel"
    ) {
        result = "Perdiste";
    } else if (
        playerOption === "📄 Papel" &&
        computerOption === "✂️ Tijera"
    ) {
        result = "Perdiste";
    } else if (
        playerOption === "✂️ Tijera" &&
        computerOption === "🪨 Piedra"
    ) {
        result = "Perdiste";
    } else {
        result = "Ganaste";
    }

    console.log(result);
});