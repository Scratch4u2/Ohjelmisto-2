function leapyr(year) {
  let is_it = ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0));
  return is_it;
}

const year = prompt('Give a year')
const print = document.querySelector('p');
print.textContent = 'Is leap year: ' + leapyr(year)