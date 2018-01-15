// Create a sheep farm with 20 slots
/* const SheepFarm = new Farm(20);

console.log(SheepFarm.animals); // Should log 20 Animal objects

const button = document.querySelector('button');
 */
// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full
'use strict';
function Animal(){
  this.hunger = 5;
  this.thirst = 5;
  this.eat = function(){
    this.hunger -= 1;
  }
  this.drink = function(){
    this.thirst -= 1;
  }
  this.play = function(){
    this.hunger += 1;
    this.thirst += 1;
  }
}
var pig = new Animal();
var pig1 = new Animal();
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
    
}
function animalAdder(numberOfAnimals, toFarm){
  for(var i = 0; i < numberOfAnimals; i++){
    var animal = new Animal();
    toFarm.liveStock.push(animal)
  }
}
var farm1 = new Farm(20);
animalAdder(20, farm1);
farm1.stats();

farm1.liveStock[18].eat();
//console.log(farm1.liveStock)
farm1.slaughter();
//console.log(farm1.liveStock)
farm1.stats();
