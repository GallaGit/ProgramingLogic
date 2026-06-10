//Tipos de datos primitivos en TypeScript
const age: number = 30;
const isStudent: boolean = false;
const myName: string = "Alice"; //se puede usar con "... o con '...' o con `...`"
const uniqueId: symbol = Symbol("id");
let data: null = null;
let notAssigned: undefined;

console.log("Age:", age);
console.log("Is Student:", isStudent);
console.log("Name:", myName);
console.log("Unique ID:", uniqueId.toString());
console.log("Data:", data);
console.log("Not Assigned:", notAssigned);

//Ejemplo con Null y Undefined
interface UserProfile {
  email?: string | undefined;
  phone: string | null;
}

const user1: UserProfile = { email: "user@example.com", phone: "123-4567" };
const user2: UserProfile = { phone: null };

function isValidEmail(email: string | undefined): boolean {
  return email !== undefined && email.trim() !== "";
}

function isValidPhone(phone: string | null): boolean {
  return phone !== null && phone.trim() !== "";
}

function displayContactInfo(user: UserProfile): string {
  const emailDisplay = user.email ?? "No email provided";
  const phoneDisplay = user.phone ?? "No phone provided";
  return `Email: ${emailDisplay}, Phone: ${phoneDisplay}`;
}

// Test cases
console.log(isValidEmail(user1.email)); // true
console.log(isValidEmail(undefined)); // false
console.log(isValidPhone(user1.phone)); // true
console.log(isValidPhone(user2.phone)); // false
console.log(displayContactInfo(user1)); // Email: user@example.com, Phone: 123-4567
console.log(displayContactInfo(user2)); // Email: No email provided, Phone: No phone provided


