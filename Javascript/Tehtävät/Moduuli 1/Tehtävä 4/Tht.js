function sortingHat() {
  let num = Math.floor((Math.random() * 4) + 1);
  if (num === 1) {
    return 'Gryffindor';
  } else if (num === 2) {
    return 'Slytherin';
  } else if (num === 3) {
    return 'Hufflepuff';
  } else if (num === 4) {
    return 'Ravenclaw';
  }
}

const name = prompt('What is your name');
const print = document.querySelector('p');
print.textContent = name + ', your house is ' + sortingHat();