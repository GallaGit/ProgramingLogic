const counter = document.getElementById("counter");
const increaseBtn = document.getElementById("increaseBtn");
const resetBtn = document.getElementById("resetBtn");
const decreaseBtn = document.getElementById("decreaseBtn");
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
decreaseBtn?.addEventListener("click", () => {
    valor--;
    if (counter) {
        counter.textContent = String(valor);
    }
});
