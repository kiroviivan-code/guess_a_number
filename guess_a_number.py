#NBTG

import random

x=random.randint(1,100)

print("I will choose a random number. You place your guesses. I will guide you. Good лук!")

while 1:
    a=input('Guess the number [1,100]: ')

    if not a.isdigit():
        print('A number [1,100]!!!!')
        continue
    else:
        a=int(a)

    if a==x:
        print('You guessed it!')
        break
    elif a<x:
        print('Too low!')
    else:
        print('Too high!')

