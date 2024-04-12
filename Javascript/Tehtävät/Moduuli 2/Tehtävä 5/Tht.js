let numbers = [];

function asker() {
  let num;
  while ((num = prompt('Give a number')) !== null) {
    if(numbers.includes(parseInt(num))){
      break;
    } else {
      numbers.push(parseInt(num));
    }
  }
}

asker();

const many = numbers.length;
let ordered = numbers.sort();

console.log(ordered);
