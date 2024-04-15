let rolls = []
function diceroll() {
    let num = 0;
    while (num !== 6) {
        num = Math.ceil(Math.random() * 6);
        rolls.push(num);
    }
}

diceroll();
const print = document.querySelector('ul');
for (let i = 0; i < rolls.length; i++) {
          const li = document.createElement('li');
          li.textContent = rolls[i];
          print.appendChild(li);
        }