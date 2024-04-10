function roll(dicenum){
  sum = 0
  for(i=0; i<dicenum;i++){
    let num = Math.floor(Math.random() * 6) + 1;
    sum = sum + num
  }
  return sum
}
const dice = prompt("How many dice")
console.log(roll(dice))