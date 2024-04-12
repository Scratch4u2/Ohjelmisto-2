function reverseArray(array) {
  let reversedArray = [];
  for (let i = array.length - 1; i >= 0; i--) {
    reversedArray.push(array[i]);
  }
  console.log(reversedArray);
}

let userArray = [];

function numbers() {
  for (let i = 0; i < 5; i++) {
    let num = prompt('Give a number');
    userArray.push(parseInt(num));
  }
}
numbers();
reverseArray(userArray);
