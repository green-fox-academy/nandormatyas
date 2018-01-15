// Create a sheep farm with 20 slots
/* const SheepFarm = new Farm(20);

console.log(SheepFarm.animals); // Should log 20 Animal objects

const button = document.querySelector('button');
 */
// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full
'use strict';

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function Animal(){
  this.hunger = 5;
  this.thirst = 5;
  this.eat = function(){
    this.hunger -= getRandomInt(4);
  }
  this.drink = function(){
    this.thirst -= getRandomInt(4);
  }
  this.play = function(){
    this.hunger += getRandomInt(4);
    this.thirst += getRandomInt(4);
  }
}

function Farm(totalSlot){
  this.totalSlot = totalSlot;
  this.liveStock = [];
  this.breed = function (animal){
    if(this.liveStock.length < this.totalSlot){
      this.liveStock.push(animal);
    }else{
      console.log('No more space for new animal!')
    }
  }
  this.slaughter = function (){
    var lowHunger = 100;
    for(var i = 0; i < this.liveStock.length; i++){
      if(this.liveStock[i].hunger < lowHunger){
        lowHunger = this.liveStock[i].hunger;
      }
    }
    for(var j = 0; j < this.liveStock.length; j++){
      if(this.liveStock[j].hunger === lowHunger){
        this.liveStock.splice(j, 1);
      }
    }
  }
  this.stats = function(){
    console.log('The farm has ' + this.liveStock.length + ' living animals');
  }
  //RANDOM EVENT HAPPENS TO EACH ANIMAL
  this.progress = function(){
    var happenings = ['eat', 'drink', 'play'];
    for(var i = 0;i< this.liveStock.length;i++){
      var event = this.liveStock[i]
      var thing = happenings[getRandomInt(3)];
      event[thing]();
    }
    this.stats()
    this.slaughter();
    this.stats()
    this.breed(new Animal());
    this.stats()
  }
  
}
//FILL UP FARM WITH ANIMALS
function animalAdder(numberOfAnimals, toFarm){
  for(var i = 0; i < numberOfAnimals; i++){
    var animal = new Animal();
    toFarm.liveStock.push(animal)
  }
}

var farm1 = new Farm(20);
animalAdder(20, farm1);

//farm1.stats();
farm1.progress();
//console.log(farm1.liveStock);
//farm1.stats();
//farm1.slaughter();

//farm1.stats();
