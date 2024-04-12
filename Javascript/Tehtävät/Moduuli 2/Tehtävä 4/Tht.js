let numbers = [];

function asker() {
  let num;
  while ((num = prompt('Give a number')) !== '0') {
    numbers.push(parseInt(num));
  }
}

asker();

const many = numbers.length;
let ordered = numbers.sort((a, b) => b - a);

console.log(ordered);
