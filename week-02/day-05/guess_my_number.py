''' Exercise

Write a program where the program chooses a number between 1 and 100. The player is then asked to enter a guess. If the player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.

    Make the range customizable (ask for it before starting the guessing).
    You can add lives. (optional)
 '''
import random

lives = 5
rang1, rang2 = input('In what range do you want to guess? (ex:1 100): ').split()
rang1, rang2 = int(rang1), int(rang2)

numberx = random.randrange(rang1, rang2)
print('You have five lives')
while lives > 0:
    guess = int(input('Guess the number: '))
    if guess < numberx:
        print('The stored number is higher')
        lives -= 1
        print('Lives left: ', lives)
        #continue
    elif guess > numberx:
        print('The stored number is lower')
        lives -= 1
        print('Lives left: ', lives)

    elif guess == numberx:
        print('You found the number:',numberx)
        print('Well done!')
        break

if lives == 0:
    print('Game Over')
    print('The number was: ', numberx)



