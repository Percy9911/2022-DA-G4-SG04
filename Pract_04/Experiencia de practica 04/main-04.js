let perro = 
{
    edad: 4,
    nombre: 'Bobby',
    nacimiento: 2021,
    raza: 'Bulldog'
};
console.log(perro['nombre']);
console.log(perro['edad']);
console.log(perro['nacimiento']);
console.log(perro['raza']);

let perro2 = new Object();

perro2.nombre = 'Cady';
perro2.edad = 2;
perro2.nacimiento = 2022;
perro2.raza = 'cavalier';

console.log(perro2['nombre']);
console.log(perro2['edad']);
console.log(perro2['nacimiento']);
console.log(perro2['raza']);

let perro3 = Object.create(perro);
console.log(perro3['nombre']);
console.log(perro3['edad']);
console.log(perro3['nacimiento']);
console.log(perro3['raza']);