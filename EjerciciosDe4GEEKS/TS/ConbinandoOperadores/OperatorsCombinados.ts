/*const age: number = 30;
const hasHighSchoolDiploma: boolean = true;
const yearsExperience: number = 3;
const isResident: boolean = false;
const hasVisa: boolean = true;

//Divide condiciones complejas en variables intermedias para mayor claridad
const isAgeEligible = age >= 18 && age <=35;
const educationOrExperience = hasHighSchoolDiploma || yearsExperience <= 2;
const residencyStatus = isResident || hasVisa;

//Conbina todas las condiciones en un parentesis para asegurar la evaluacion correcta
const isElegible = isAgeEligible && educationOrExperience && residencyStatus

console.log("Estado de Eligibilidad: ", isElegible);*/

//datos del cliente
/*const totalCompraProducto: number = 150
const hasMembership: boolean = true;
const isbirthdayMonth: boolean = false;

//datos de la empresa
const isMember: boolean= hasMembership;
const totalCompra = totalCompraProducto >= 100;
const birthdayMonth = isbirthdayMonth;

const discoutstatus = isMember && totalCompra && birthdayMonth


if (!discoutstatus) {
    console.log("No aceptado. Verifica lo siguiente:");
    
 } else if (!isMember) {
        console.log("- Debes ser miembro");
    }

    else if (!totalCompra) {
        console.log("- La compra debe ser de al menos 100€");
    }

    else if (!isbirthdayMonth) {
        console.log("- Debe ser tu mes de cumpleaños");
    }

    else {
    console.log("Aceptado: tienes el descuento");
}
    }
    
   

   
}*/

const purchaseAmount = 150;
const isMember = true;
const isBirthdayMonth = false;

// Condiciones complejas de descuento
const discount20 = isMember && (purchaseAmount > 100 || isBirthdayMonth);
const discount10 = !isMember && purchaseAmount > 200;
const discount5 = !discount20 && !discount10 && purchaseAmount > 50;

// Calcula el porcentaje de descuento
let discountPercent = 0;
if (discount20) {
  discountPercent = 20;
} else if (discount10) {
  discountPercent = 10;
} else if (discount5) {
  discountPercent = 5;
}

const discountAmount = (purchaseAmount * discountPercent) / 100;
const finalPrice = purchaseAmount - discountAmount;

console.log(`Precio final después de un descuento del ${discountPercent}%: $${finalPrice}`);

// Consejo de depuración: Usa console.log() para verificar cada condición booleana
console.log({ discount20, discount10, discount5 });