'use strict';

console.log('I have awaken!');

const name = 'Matti';
const names = ['Aku','Iines','Hannu']

console.log('Moi ' + name)
console.log('Nimet ' + names)

const firstP = document.querySelector('p');
console.log(firstP);
firstP.textContent = 'Hei ' + name;

const allP = document.querySelectorAll('p');
console.log(allP)
allP.textContent[1].textContent = 'Hei' + 'Lukija';
