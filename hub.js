const exercises = [
    {
        id: 1,
        title: "Fizz Buzz",
        desc: "Sustituye multiplos de 3 y 5 por Fizz y Buzz.",
        href: "Ejercicios/NivelFacil/Fizz-Buzz/index.html",
        icon: "🎯",
        status: "done",
        statusLabel: "Terminado",
        accent: "#ff6b4a",
    },
    {
        id: 2,
        title: "Contador",
        desc: "Suma, resta y reinicia con botones [+] y [-].",
        href: "Ejercicios/NivelFacil/Contador/index.html",
        icon: "🔢",
        status: "done",
        statusLabel: "Terminado",
        accent: "#2ec4b6",
    },
    {
        id: 3,
        title: "Convertidor Universal",
        desc: "De Celsius a Fahrenheit… y luego a convertidor universal.",
        href: "Ejercicios/NivelFacil/Convertidores/index.html",
        icon: "🌡️",
        status: "scaled",
        statusLabel: "Escalado",
        accent: "#9ef01a",
    },
    {
        id: 4,
        title: "Calculadora",
        desc: "Operaciones basicas con una calculadora simple.",
        href: "Ejercicios/NivelMedio/Calculadora/index.html",
        icon: "🧮",
        status: "done",
        statusLabel: "Terminado",
        accent: "#ffd166",
    },
    {
        id: 5,
        title: "Generador de Contraseñas",
        desc: "Genera contraseñas segun la longitud que indiques.",
        href: "Ejercicios/NivelMedio/GeneradorDeContraseñas/index.html",
        icon: "🔐",
        status: "done",
        statusLabel: "Terminado",
        accent: "#7bdff2",
    },
    {
        id: 6,
        title: "Piedra, Papel, Tijera",
        desc: "Juega contra la PC: elige, compara y ve quien gana.",
        href: "Ejercicios/NivelMedio/piedra-papel-tigera/index.html",
        icon: "✂️",
        status: "progress",
        statusLabel: "En progreso",
        accent: "#ff8f6b",
    },
    {
        id: 7,
        title: "Anagrama",
        desc: "¿Dos palabras tienen las mismas letras?",
        href: "Ejercicios/NivelFacil/Anagrama/index.html",
        icon: "🔤",
        status: "next",
        statusLabel: "Por hacer",
        accent: "#ff6b4a",
    },
    {
        id: 8,
        title: "Fibonacci",
        desc: "Genera los primeros N numeros de la sucesion.",
        href: "Ejercicios/NivelFacil/Fibonacci/index.html",
        icon: "🌀",
        status: "next",
        statusLabel: "Por hacer",
        accent: "#2ec4b6",
    },
    {
        id: 9,
        title: "Es primo?",
        desc: "Comprueba si un numero solo se divide por 1 y por si mismo.",
        href: "Ejercicios/NivelFacil/EsPrimo/index.html",
        icon: "➗",
        status: "next",
        statusLabel: "Por hacer",
        accent: "#ffd166",
    },
    {
        id: 10,
        title: "Contando palabras",
        desc: "Cuenta cuantas veces aparece cada palabra en un texto.",
        href: "Ejercicios/NivelFacil/ContandoPalabras/index.html",
        icon: "📝",
        status: "next",
        statusLabel: "Por hacer",
        accent: "#7bdff2",
    },
    {
        id: 11,
        title: "Tres en raya",
        desc: "Tablero 3x3, turnos y victoria en linea.",
        href: "Ejercicios/NivelMedio/TresEnRaya/index.html",
        icon: "⭕",
        status: "next",
        statusLabel: "Por hacer",
        accent: "#ff8f6b",
    },
    {
        id: 12,
        title: "Adivina el numero",
        desc: "Mas alto, mas bajo… hasta acertar el secreto.",
        href: "Ejercicios/NivelMedio/AdivinaElNumero/index.html",
        icon: "🎲",
        status: "next",
        statusLabel: "Por hacer",
        accent: "#9ef01a",
    },
    {
        id: 13,
        title: "Palindromo",
        desc: "¿Se lee igual al derecho y al reves?",
        href: "Ejercicios/NivelMedio/Palindromo/index.html",
        icon: "🔁",
        status: "next",
        statusLabel: "Por hacer",
        accent: "#2ec4b6",
    },
    {
        id: 14,
        title: "Expresiones equilibradas",
        desc: "Parentesis, corchetes y llaves bien cerrados (pila).",
        href: "Ejercicios/NivelMedio/ExpresionesEquilibradas/index.html",
        icon: "🧱",
        status: "next",
        statusLabel: "Por hacer",
        accent: "#ffd166",
    },
    {
        id: 15,
        title: "Laberinto",
        desc: "Encuentra el camino en una matriz 2D. Nivel dificil.",
        href: "Ejercicios/NivelDificil/Laberinto/index.html",
        icon: "🗺️",
        status: "next",
        statusLabel: "Dificil",
        accent: "#ff6b4a",
    },
    {
        id: 16,
        title: "Sudoku",
        desc: "Valida (y luego resuelve) un tablero 9x9.",
        href: "Ejercicios/NivelDificil/Sudoku/index.html",
        icon: "🧩",
        status: "next",
        statusLabel: "Dificil",
        accent: "#1a2332",
    },
    {
        id: 17,
        title: "MiniApp componentes",
        desc: "Proyecto pequeño con framework (React + componentes).",
        href: "Proyectos/MiniApp-Componentes/README.md",
        icon: "⚛️",
        status: "next",
        statusLabel: "Proyecto",
        accent: "#7bdff2",
    },
];

const badgeClass = {
    done: "done",
    scaled: "scaled",
    progress: "progress",
    next: "next",
};

function isCompleted(status) {
    return status === "done" || status === "scaled";
}

function renderStations() {
    const list = document.getElementById("stations");
    if (!list) return;

    list.innerHTML = exercises
        .map((ex, index) => {
            const badge = badgeClass[ex.status] || "next";
            return `
            <li class="station" style="--accent: ${ex.accent}; animation-delay: ${0.08 * index}s">
                <a class="station-btn" href="${ex.href}" data-id="${ex.id}">
                    <div class="station-top">
                        <span class="station-num">Nivel ${String(ex.id).padStart(2, "0")}</span>
                        <span class="badge ${badge}">${ex.statusLabel}</span>
                    </div>
                    <span class="station-icon" aria-hidden="true">${ex.icon}</span>
                    <h3 class="station-title">${ex.title}</h3>
                    <p class="station-desc">${ex.desc}</p>
                    <span class="station-go">Abrir →</span>
                </a>
            </li>`;
        })
        .join("");
}

function updateProgress() {
    const logic = exercises.filter((ex) => ex.id <= 16);
    const done = logic.filter((ex) => isCompleted(ex.status)).length;
    const logicTotal = logic.length;
    const pct = Math.round((done / logicTotal) * 100);

    const label = document.getElementById("progress-label");
    const pctEl = document.getElementById("progress-pct");
    const fill = document.getElementById("progress-fill");

    if (label) label.textContent = `${done} / ${logicTotal} logica terminados`;
    if (pctEl) pctEl.textContent = `${pct}%`;
    if (fill) {
        requestAnimationFrame(() => {
            fill.style.width = `${pct}%`;
        });
    }
}

function addRipple(event, target) {
    const rect = target.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const ripple = document.createElement("span");
    ripple.className = "ripple";
    ripple.style.width = `${size}px`;
    ripple.style.height = `${size}px`;
    ripple.style.left = `${event.clientX - rect.left - size / 2}px`;
    ripple.style.top = `${event.clientY - rect.top - size / 2}px`;
    target.appendChild(ripple);
    ripple.addEventListener("animationend", () => ripple.remove());
}

function wireInteractions() {
    document.querySelectorAll(".station-btn").forEach((btn) => {
        btn.addEventListener("click", (event) => {
            const station = btn.closest(".station");
            if (station) {
                station.classList.remove("bounce");
                void station.offsetWidth;
                station.classList.add("bounce");
            }
            addRipple(event, btn);
        });
    });
}

renderStations();
updateProgress();
wireInteractions();
