'use strict';

console.log('I have awaken!');

let name = 'Matti';
const names = ['Aku','Iines','Hannu']

let age, height;
age = 5;
console.log(age, typeof age, height, typeof height)

//num -> string
age = age.toString()
console.log(age.toString());
//string->num
console.log(age);

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

