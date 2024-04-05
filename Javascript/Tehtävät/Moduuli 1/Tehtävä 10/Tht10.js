function rollDice() {
    return Math.random() * 6;
}

function probability(numdice, sumeyes){
    let correct = 0

    for (let i = 0; i<10000; i++){
        let throwsum = 0
        for (let j = 0; j < numdice; j++){
            throwsum += rollDice()
        }
        if (throwsum === sumeyes){
            correct += 1
        }
        else {

        }
    }
    return correct / 10000
}
const numdice = parseInt(prompt("Number of dice"))
const sumeyes = parseInt(prompt("Wanted eyesum"))
const answer = probability(numdice,sumeyes).toFixed(2) * 100
const print = document.querySelector('p')
print.textContent = 'Probability of ' + sumeyes + ' with ' + numdice + ' dice is: ' + answer + '%';
