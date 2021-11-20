// prediction button event
const predictions = document.querySelector('#predictions');
predictions.addEventListener('click', (e) => {
  e.preventDefault();
  document.querySelector('#main').innerHTML = 'Predictions'
})

// results button event
const results = document.querySelector('#results');
results.addEventListener('click', (e) => {
  e.preventDefault();
  document.querySelector('#main').innerHTML = 'Results'
})

// standings button event
const standings = document.querySelector('#standings');
standings.addEventListener('click', (e) => {
  e.preventDefault();
  document.querySelector('#main').innerHTML = 'Standings'
})
