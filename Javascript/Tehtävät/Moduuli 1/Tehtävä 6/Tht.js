let what = confirm('Do you want the square root');
if (what === true) {
  const num = prompt('Give a number for square root');
  let root = Math.sqrt(num);
  const print = document.querySelector('p');
  print.textContent = 'square root of ' + num + ' is ' + root;
} else {
  const print = document.querySelector('p');
  print.textContent = 'The square root is not calculated.';
}