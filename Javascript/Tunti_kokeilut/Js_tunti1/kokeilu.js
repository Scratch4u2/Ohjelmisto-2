'use strict';

console.log('I have awaken!');

let name = 'Matti';
const names = ['Aku','Iines','Hannu']

let age, height;
age = 5.2;
console.log(age, typeof age, height, typeof height)

console.log(name + ' ikä on ' + age + '-vuotta')
console.log(`${name}:n ikä on ${age}-vuotta`);

//num -> string
age = age.toString()
console.log(age);
//string->num
//age = 'viisi vuotta'; niin tulee Nan=not a number mutta menee läpi
age = parseFloat(age);
console.log(age);

const ageAdd = 3;
age++;

const underAge = true;
console.log(underAge, typeof underAge)

console.log('Moi ' + name)
console.log('Nimet ' + names)

const firstP = document.querySelector('p');
console.log(firstP);
firstP.textContent = 'Hei ' + name;

const allP = document.querySelectorAll('p');
console.log(allP)
allP[3].textContent = 'Hei ' + 'Lukija';


//name = prompt('Anna nimi:');
//console.log(name)

console.log(Math.random())
console.log(Math.floor(Math.random()*6+1))