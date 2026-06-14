"use strict";
const counter = document.getElementById("counter");
const increaseBtn = document.getElementById("increaseBtn");
const resetBtn = document.getElementById("resetBtn");
let valor = 0;
increaseBtn?.addEventListener("click", () => {
    valor++;
    if (counter) {
        counter.textContent = String(valor);
    }
});
resetBtn?.addEventListener("click", () => {
    valor = 0;
    if (counter) {
        counter.textContent = String(valor);
    }
});
