function concat(array) {
  let concatArray = ''
  for(i=0;i<array.length;i++)
    concatArray = concatArray + array[i]
  return concatArray
}

const example = ['Johnny', 'DeeDee', 'Joey', 'Marky'];

const print = document.querySelector('p');
print.textContent = concat(example)
