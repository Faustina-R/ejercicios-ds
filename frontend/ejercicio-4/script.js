let total = 0;

const display = document.getElementById("numero");
const btnDisminuir = document.getElementById("btnMenos");
const btnAumentar = document.getElementById("btnMas");

btnAumentar.addEventListener("click", () => {
  total++;
  display.textContent = total;
});

btnDisminuir.addEventListener("click", () => {
  total--;
  display.textContent = total;
});