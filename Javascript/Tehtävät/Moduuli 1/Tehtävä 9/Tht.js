function isPrime(number) {
    let inum = false;
    if (number <= 1) {
        inum = false;
    } else if (number <= 3) {
        inum = true;
    } else {
        for (let i = 2; i < number; i++) {
            if (number % i === 0) {
                inum = false;
                break;
            } else {
                inum = true;
            }
        }
    }
    return inum;
}

const usernum = prompt("Give a number")
const print = document.querySelector('p');
print.textContent = 'is number:' + usernum + ' prime: ' + isPrime(usernum)