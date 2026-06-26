const chars : string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
const lengthInput = document.getElementById("length") as HTMLInputElement;   
const passLength: number = Number(lengthInput.value);
const results = document.getElementById("result") as HTMLParagraphElement;
let password: string = "";


for(let i = 0; i < passLength; i++){ 
  const randomIndex = Math.floor(Math.random() * chars.length)
  const randomChar: string = chars[randomIndex];
  password += randomChar;
  
}

results.textContent = password;
