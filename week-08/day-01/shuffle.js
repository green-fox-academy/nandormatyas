const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
      this.cash += amt;
    }
}
const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt){
      this.cash += amt;
    }

}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

const Shuffler = {
    cash: 10000,
    pick: function() {
      offshores = [Panama, Cyprus];
      which = offshores[getRandomInt(2)];
      which.deposit(1000);
      this.cash -= 1000;
      console.log(which.name + ' got ' + '1000')
    }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 