const names = [];

names[0] = 'Aku';
names[1] = 'Iines';
console.log(names);

names.push('Roope');
console.log(names);

names.pop();
console.log(names);

const lastName = names.pop();
console.log(names);
console.log(lastName);

const ages = [4, 5, 6];
//console.log(ages.length)

for (let i = 0; i < ages.length; i++) {
  console.log(ages[i]);
}

for (const name of names) {
  console.log(name);
}
//kääntää
ages.reverse();
console.log(ages);
//kääntää takaisin
console.log(ages.toReversed());

const searchParam = 'Aku';

if (names.includes(searchParam)) {
  console.log(searchParam + ' löytyi');
  console.log(names.indexOf(searchParam));
} else {
  console.log(searchParam + ' Ei löytynyt');
}
