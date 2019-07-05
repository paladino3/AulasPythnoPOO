"""
Projeto Jogo da forca   Com Random, time , e Lista strings
"""

import time
import random

name = str(input('What is your name? ')).lower()
print('Hello, {} Time to play hangman!\n'.format(name))

time.sleep(1)

print('Start guessing...')

time.sleep(0.5)

listOfWords = ['devemedia','secret','cat','trash','python']

randomNumber = random.randint(0,len(listOfWords) - 1) #menos 1 porque as lista iniciam da posição (0,1,2,3,4)

guessWord = listOfWords[randomNumber]
word = guessWord
guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed +=1

    if failed == 0:
        print('\nYou win')
        break
    print('')
    guess = str(input('guess a character: '))

    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong \n')
        print('You have {}, more guesses'.format(turns))

        if turns == 0:
            print('You Lose!')