function locationsuccess (){
  console.log("Käyttäjä paikannettu")
}
function locationError(){
    console.log("Käyttäjää ei löydetty")

}

const locationOptions = {
  timeout: 1000
}

navigator.geolocation.getCurrentPosition(locationsuccess);