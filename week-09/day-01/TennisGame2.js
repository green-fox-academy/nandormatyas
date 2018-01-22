'use strict';

let PlayersSetup = function(player1Name, player2Name) {
    this.player1Points = 0;
    this.player2Points = 0;

    this.player1Results = "";
    this.player2Results = "";

    this.player1Name = player1Name;
    this.player2Name = player2Name;
};

PlayersSetup.prototype.getScore = function() {
    let score = "";
    let scoreTable = {
      0: 'Love',
      1: 'Fifteen',
      2: 'Thirty',
      3: 'Forty'
    };

    if (this.player1Points === this.player2Points && this.player1Points < 3) {
      score = scoreTable[this.player1Points]
      score += "-All";

    }
    if (this.player1Points === this.player2Points && this.player1Points > 2)
        score = "Deuce";

    if (this.player1Points > 0 && this.player2Points === 0) {
      this.player1Results = scoreTable[this.player1Points];

        this.player2Results = "Love";
        score = this.player1Results + "-" + this.player2Results;
    }
    if (this.player2Points > 0 && this.player1Points === 0) {
      this.player2Results = scoreTable[this.player2Points];

        this.player1Results = "Love";
        score = this.player1Results + "-" + this.player2Results;
    }

    if (this.player1Points > this.player2Points && this.player1Points < 4) {
      this.player1Results = scoreTable[this.player1Points];
      this.player2Results = scoreTable[this.player2Points];
  
        score = this.player1Results + "-" + this.player2Results;
    }
    if (this.player2Points > this.player1Points && this.player2Points < 4) {
      this.player1Results = scoreTable[this.player1Points];
      this.player2Results = scoreTable[this.player2Points];

        score = this.player1Results + "-" + this.player2Results;
    }

    if (this.player1Points > this.player2Points && this.player2Points >= 3) {
        score = "Advantage player1";
    }

    if (this.player2Points > this.player1Points && this.player1Points >= 3) {
        score = "Advantage player2";
    }

    if (this.player1Points >= 4 && this.player2Points >= 0 && (this.player1Points - this.player2Points) >= 2) {
        score = "Win for player1";
    }
    if (this.player2Points >= 4 && this.player1Points >= 0 && (this.player2Points - this.player1Points) >= 2) {
        score = "Win for player2";
    }
    return score;
};

PlayersSetup.prototype.SetP1Score = function(number) {
    for (let i = 0; i < number; i++) {
        this.P1Score();
    }
};

PlayersSetup.prototype.SetP2Score = function(number) {
    for (let i = 0; i < number; i++) {
        this.P2Score();
    }
};

PlayersSetup.prototype.P1Score = function() {
    this.player1Points++;
};

PlayersSetup.prototype.P2Score = function() {
    this.player2Points++;
};

PlayersSetup.prototype.wonPoint = function(player) {
    if (player === "player1")
        this.P1Score();
    else
        this.P2Score();
};

if (typeof window === "undefined") {
    module.exports = PlayersSetup;
}