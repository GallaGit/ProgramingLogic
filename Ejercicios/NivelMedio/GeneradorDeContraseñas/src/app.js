"use strict";
const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
const lengthInput = document.getElementById("length");
const passLength = Number(lengthInput.value);
const results = document.getElementById("result");
let password = "";
for (let i = 0; i < passLength; i++) {
    const randomIndex = Math.floor(Math.random() * chars.length);
    const randomChar = chars[randomIndex];
    password += randomChar;
}
results.textContent = password;
