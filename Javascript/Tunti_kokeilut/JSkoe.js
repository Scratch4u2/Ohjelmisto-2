function weather(condition){
  if(condition === true){
    return 'umbrella'
  }
  else{
    return 'sunglasses'
  }
}


function average(array){
  let sum = 0
  for(let i = 0; i<array.length;i++){
    sum = sum + array[i]
  }
  return sum / array.length
}