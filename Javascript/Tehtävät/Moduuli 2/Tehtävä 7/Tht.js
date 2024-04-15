let rolls = []
function diceroll(sides) {
    let num = 0;
    while (num !== sides) {
        num = Math.ceil(Math.random() * sides);
        rolls.push(num);
    }
}

const sides = parseInt(prompt('How many sides does the dice have'))
diceroll(sides);
const print = document.querySelector('ul');
for (let i = 0; i < rolls.length; i++) {
          const li = document.createElement('li');
          li.textContent = rolls[i];
          print.appendChild(li);
        }