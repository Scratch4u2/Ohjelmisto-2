let participants = []
function number(){
  const num = prompt('How many paricipants')
  for(i=0;i<num;i++){
    let name = prompt('Name of one participant')
    participants.push(name)
  }
}

number()
const ordered = participants.sort()
const print = document.querySelector('ol');
for (let i = 0; i < ordered.length; i++) {
          const li = document.createElement('li');
          li.textContent = ordered[i];
          print.appendChild(li);
        }