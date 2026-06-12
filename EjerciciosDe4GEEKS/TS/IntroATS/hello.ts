/*const greetings: string = "Hola, TyoeScript!";
const year: number = 2026;
const isLearning: boolean = true;

console.log(greetings) 
console.log("Año: ", year);
console.log("Estoy aprendiendo?", isLearning)

console.log("-------------------------------");

const nombreUsuario: string = "Maria";
console.log("Nombre de Usuario:", nombreUsuario);  // Salida: Nombre de Usuario: Maria

// Variable numérica
let edadUsuario: number = 28;
console.log("Edad del Usuario:", edadUsuario);  // Salida: Edad del Usuario: 28

// Variable booleana
const esEstudiante: boolean = true;
console.log("Es Estudiante:", esEstudiante);  // Salida: Es Estudiante: true

console.log("-------------------------------");

let colorFavorito: string;
colorFavorito = "azul";
console.log("Color Favorito:", colorFavorito);

console.log("-------------------------------");

const profileName: string = "Ociel Gallardo";
const age: number = 35;
const isMember: boolean = true;

console.log("Name: ", profileName);
console.log(" Age: ", age)
console.log("Have a membership: ", isMember);

console.log("-------------------------------");

const postAuthor: string = "Alice";
let postLikes: number = 0;
const isPostPublic: boolean = true;

postLikes += 1;

console.log(`Publicación de ${postAuthor} tiene ${postLikes} likes. Público: ${isPostPublic}`);
//este console.log tambien se puede usar en js


//Tipos de datos primitivos en TypeScript
const age: number = 30;
const isStudent: boolean = false;
const myName: string = "Alice"; //se puede usar con "... o con '...' o con `...`"
const uniqueId: symbol = Symbol("id");
let data: null = null;
let notAssigned: undefined;*/


//operadores de comparación para tomar decisiones en el código

//Operadores de comparación
/* Igualdad y Desigualdad:
== (igualdad débil)
=== (igualdad estricta)
!= (desigualdad débil)
!== (desigualdad estricta)
*/
//diferencia entre == y ===
/*const num: number = 5;
console.log(num=="5");  // true, porque == realiza una comparación de igualdad débil (coerción de tipos)
console.log(num==="5"); // false, porque === realiza una comparación de igualdad estricta (sin coerción de tipos)

//Operadores de relacionales
/* 
> (mayor que)
< (menor que)
>= (mayor o igual que)
<= (menor o igual que)
estos se usan para crear exprosiones booleanas que controlan el flujo del programa, como en condicionales o bucles.
*/
/*const edad: number = 25;
if (edad >= 18) {
    console.log("Eres mayor de edad.");
} else {
    console.log("Eres menor de edad.");
}   */

/* Evita encadenar comparaciones como 18 <= edad <= 65. Esto no funciona como se espera en TypeScript.
En su lugar, usa operadores lógicos para combinar comparaciones:
*/
/*if (edad >= 18 && edad <= 65) {
    console.log("Edad Laboral.");
}
*/
//Operadores logicos
/*
&& (AND lógico): Devuelve true si ambos operandos son verdaderos.
|| (OR lógico): Devuelve true si al menos uno de los operandos es verdadero.
! (NOT lógico): Invierte el valor de verdad del operando.
*/
const isLoggedIn  = true;
const hasNotifications = false;
const showNotificationBadge = isLoggedIn && hasNotifications;
console.log(showNotificationBadge); // false

const isFriend = false;
const isFollowing = true;
const canViewStory = isFriend || isFollowing;
console.log(canViewStory); // true

const isPrivateAccount = true;
const canSendMessage = !isPrivateAccount;
console.log(canSendMessage); // false