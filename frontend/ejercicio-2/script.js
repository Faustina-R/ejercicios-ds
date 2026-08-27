const input = document.getElementById("inputTarea");
const boton = document.getElementById("btnAgregar");
const lista = document.getElementById("listaTareas");

function guardarTarea() {
  const texto = input.value.trim();
  if (texto === "") return;

  const item = document.createElement("li");
  item.textContent = texto;

  item.addEventListener("click", () => {
    item.remove();
  });

  lista.appendChild(item);
  input.value = "";
  input.focus();
}

boton.addEventListener("click", guardarTarea);

input.addEventListener("keypress", (evento) => {
  if (evento.key === "Enter") {
    guardarTarea();
  }
});