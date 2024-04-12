
function locationSuccess (location) {
    console.log('Käyttäjä paikannettu', location);
  }
  
  function locationError (error) {
    console.log('paikannus fail', error);
  }
  
  const locationOptions = {
    timeout: 3000
  };
  
  function locateUser() {
    navigator.geolocation.getCurrentPosition(locationSuccess, locationError, locationOptions);
}
  
  console.log('Moro!');
  
  // DOM-kikkailua
  
  const section2 = document.querySelectorAll('section')[1];
  const pElement = section2.querySelector('p');
  pElement.textContent = 'muokattu';
  
  const newP = document.createElement('p');
  newP.textContent = 'uusi kappale';
  section2.append(newP);
  // newP.style = 'color: blue';
  newP.classList.add('blue');

  const thirdSection = document.querySelector('#third-section');
  thirdSection.innerHTML = `
      <h2>Kolmannen osion otsikko</h2>
      <p>
          Tässä taas tekstiä.
      </p>`;

// Tapahtuman käsittely

const buttonElement = document.querySelector('button');
buttonElement.addEventListener('click', function() {
    console.log('painettu napulaa');
    // newP.classList.add('red');
    // newP.classList.remove('blue');
    newP.classList.toggle('red');
    newP.classList.toggle('blue');
});

document.addEventListener['keypress',locateUser]