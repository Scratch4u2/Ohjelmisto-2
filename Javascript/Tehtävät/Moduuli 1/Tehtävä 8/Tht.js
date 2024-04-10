leapyears = [];

function leapyr(start, end) {
  for (let i = start; i < end; i++) {
    if (i % 4 == 0) {
      leapyears.push(i);
    }
  }
}

const startyr = prompt('Start year');
const endyr = prompt('End year');
leapyr(startyr, endyr)
const listContainer = document.getElementById('lista');
leapyears.forEach(item => {
  const listItem = document.createElement('li')
  listItem.textContent = item;
  listContainer.appendChild(listItem);
})
