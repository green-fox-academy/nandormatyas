/*  Remove the king from the list.
    Fill the list based on the following list of objects.
    Only add the asteroids to the list.
    Each list item should have its category as a class and its content as text content. -->
 */
var asteroids = document.querySelector('.asteroids');
var king = document.querySelector('li');
var removed = asteroids.removeChild(king);


const planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]

/* Fill the list based on the following list of objects.
Only add the asteroids to the list.
Each list item should have its category as a class and its content as text content. -->
 */
for(var i = 0; i < planetData.length; i++){
  if(planetData[i].asteroid === true){
    var asteroid = document.createElement('li');
    asteroid.setAttribute('class', planetData[i].category);
    asteroid.innerHTML = planetData[i].content;
    asteroids.appendChild(asteroid);
  }
}
