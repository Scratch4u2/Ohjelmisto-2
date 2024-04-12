const search = document.querySelector('#search');
search.addEventListener('submit', async function(event) {
  event.preventDefault();

  const value_from_input = document.querySelector('#query').value;
  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value_from_input}`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log('Error:', error);
  }
});