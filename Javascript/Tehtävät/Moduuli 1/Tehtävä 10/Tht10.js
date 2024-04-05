function rollDice(numdice) {
    return Math.floor(Math.random() * 6) + 1;
}

function propability(numdice, sumeyes){
    let correct = 0

    for (let i; i<10000; i++){
        let throwsum = 0
        for (let j; j < numdice; j++){
            sum += rollDice()
        }
        if (sum === sumeyes){
            correct += 1
        }
        else {

        }
    }
    return correct / 10000
}
const numdice = parseInt(prompt("Number of dice"))
const sumeyes = parseInt(prompt("Wanted eyesum"))
const answer = propability(numdice,sumeyes)
const print = document.querySelector('p')
print.textContent = 'Propability of' + sumeyes + 'with' + numdice + 'dice is:' + answer;
