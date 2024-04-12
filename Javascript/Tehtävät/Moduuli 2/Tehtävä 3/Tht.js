let dogs = []
function names(){
  for(i=0;i<6;i++){
    let name = prompt('Name of one dog')
    dogs.push(name)
  }
}

names()
const ordered = dogs.sort((a,b) => b.localeCompare(a))
const print = document.querySelector('ul');
for (let i = 0; i < ordered.length; i++) {
          const li = document.createElement('li');
          li.textContent = ordered[i];
          print.appendChild(li);
        }