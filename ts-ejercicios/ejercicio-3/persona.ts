interface Persona {
  nombre: string;
  edad: number;
}

const estudiante: Persona = {
  nombre: "Franco",
  edad: 24,
};

console.log(`Nombre: ${estudiante.nombre}`);
console.log(`Edad: ${estudiante.edad}`);