function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

function probability(numDice, sumEyes) {
    let correct = 0;

    for (let i = 0; i < 10000; i++) {
        let throwSum = 0;
        for (let j = 0; j < numDice; j++) {
            throwSum += rollDice();
        }
        if (throwSum === sumEyes) {
            correct += 1;
        }
    }

    return correct / 10000;
}

const numDice = parseInt(prompt("Number of dice:"));
const sumEyes = parseInt(prompt("Sum of the eyes:"));
const answer = probability(numDice, sumEyes).toFixed(4);

const print = document.querySelector('p');
print.textContent = 'Probability of ' + sumEyes + ' with ' + numDice + ' dice is:' + (answer * 100).toFixed(1) + '%';
