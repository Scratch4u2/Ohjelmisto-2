function even(array) {
  let evenArray = [];
  for (let i = 0; i < array.length; i++) {
    if (array[i] % 2 === 0) {
      evenArray.push(array[i]);
    }
  }
  return evenArray;
}

const example = [2, 7, 4];

console.log(example);
console.log(even(example));
