"use strict";
const user1 = { email: "user@example.com", phone: "123-4567" };
const user2 = { phone: null };
function isValidEmail(email) {
    return email !== undefined && email.trim() !== "";
}
function isValidPhone(phone) {
    return phone !== null && phone.trim() !== "";
}
function displayContactInfo(user) {
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
