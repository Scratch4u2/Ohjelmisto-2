const num1  = prompt("Give number")
const num2  = prompt("Give number")
const num3  = prompt("Give number")

const product = parseInt(num1) * parseInt(num2) * parseInt(num3)
const sum = parseInt(num1) + parseInt(num2) + parseInt(num3)
const average =  sum / 3

const all = document.querySelector('p');
all.textContent = "product:" + product + " sum:" + sum + " average:" + average;
