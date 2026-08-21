const options = {
    piedra: { label: "🪨 Piedra", icon: "🪨" },
    papel: { label: "📄 Papel", icon: "📄" },
    tijera: { label: "✂️ Tijera", icon: "✂️" },
};

const keys = Object.keys(options);

const playerChoiceEl = document.getElementById("player-choice");
const pcChoiceEl = document.getElementById("pc-choice");
const resultEl = document.getElementById("result");
const arenaEl = document.getElementById("arena");
const playerScoreEl = document.getElementById("player-score");
const pcScoreEl = document.getElementById("pc-score");
const buttons = document.querySelectorAll(".play-btn");

let playerScore = 0;
let pcScore = 0;
let busy = false;

/* Flujo
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

function getComputerChoice() {
    const randomIndex = Math.floor(Math.random() * keys.length);
    return keys[randomIndex];
}

function decideWinner(player, computer) {
    if (player === computer) return "Empate";

    const playerLoses =
        (player === "piedra" && computer === "papel") ||
        (player === "papel" && computer === "tijera") ||
        (player === "tijera" && computer === "piedra");

    return playerLoses ? "Perdiste" : "Ganaste";
}

function setResultStyle(outcome) {
    resultEl.classList.remove("win", "lose", "draw", "pop");
    void resultEl.offsetWidth;

    if (outcome === "Ganaste") resultEl.classList.add("win");
    else if (outcome === "Perdiste") resultEl.classList.add("lose");
    else resultEl.classList.add("draw");

    resultEl.classList.add("pop");
}

function playRound(playerKey) {
    if (busy) return;
    busy = true;

    buttons.forEach((btn) => {
        btn.classList.toggle("active", btn.dataset.choice === playerKey);
    });

    playerChoiceEl.textContent = "❔";
    pcChoiceEl.textContent = "❔";
    resultEl.textContent = "La PC esta pensando...";
    resultEl.classList.remove("win", "lose", "draw");

    arenaEl.classList.remove("reveal");
    arenaEl.classList.add("shake");

    setTimeout(() => {
        const computerKey = getComputerChoice();
        const outcome = decideWinner(playerKey, computerKey);

        arenaEl.classList.remove("shake");
        arenaEl.classList.add("reveal");

        playerChoiceEl.textContent = options[playerKey].icon;
        pcChoiceEl.textContent = options[computerKey].icon;

        if (outcome === "Ganaste") {
            playerScore += 1;
            playerScoreEl.textContent = String(playerScore);
        } else if (outcome === "Perdiste") {
            pcScore += 1;
            pcScoreEl.textContent = String(pcScore);
        }

        resultEl.textContent =
            "Tu: " + options[playerKey].label +
            " | PC: " + options[computerKey].label +
            " → " + outcome;

        setResultStyle(outcome);
        busy = false;
    }, 450);
}

buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
        playRound(btn.dataset.choice);
    });
});
