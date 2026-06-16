//LOOPS 
//Loop Do While
//Ejemplo: Validación Simulada de Entrada de Usuario
function getUserInput(): string | null {
  const inputs = [null, '', 'entrada válida'];
  return inputs[Math.floor(Math.random() * inputs.length)];
}

let userInput: string | null;
do {
  userInput = getUserInput();
  console.log(`Usuario ingresó: ${userInput}`);
} while (!userInput || userInput.trim() === '');

console.log('Entrada válida recibida:', userInput);// Fin del bucle Do While

//Evitando Bucles Infinitos
// //Un bucle infinito ocurre si la condición nunca se vuelve falsa. Por ejemplo:

let attempts = 0;
do {
  console.log('Intentando...');
  // Falta actualizar 'attempts' causa bucle infinito
} while (attempts < 3);


//Para evitar esto, actualiza tus variables de control del bucle dentro del mismo:

let attempts = 0;
do {
  console.log('Intentando...');
  attempts++;
} while (attempts < 3);