function locationsuccess (){
  console.log("Käyttäjä paikannettu")
}

navigator.geolocation.getCurrentPosition(locationsuccess);