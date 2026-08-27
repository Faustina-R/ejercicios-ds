const formulario = document.getElementById("formRegistro");
const inputNombre = document.getElementById("campoNombre");
const inputEmail = document.getElementById("campoEmail");
const alerta = document.getElementById("alerta");

formulario.addEventListener("submit", (e) => {
  e.preventDefault();

  const nombre = inputNombre.value.trim();
  const email = inputEmail.value.trim();

  alerta.className = "alerta";

  if (nombre === "" || email === "") {
    alerta.textContent = "Todos los campos son obligatorios.";
    alerta.classList.add("error");
  } else {
    alerta.textContent = "Datos enviados correctamente.";
    alerta.classList.add("exito");
    formulario.reset();
  }
});