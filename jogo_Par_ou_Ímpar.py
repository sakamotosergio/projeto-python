from random import randint
from time import sleep

escolha = int(input('''
                    0[Par]
                    1[Impar]'''))
player = int(input('digite um numero de 0 a 100 '))
computer = randint(0,100)
s1 = (player + computer) % 2


if escolha == 0:
    if s1 == 0:
        print('YOU WIN')
    else:
        print('YOU LOSE')
elif escolha == 1:
    if s1 == 0:
        print('YOU LOSE')
    else:
        print('YOU WIN')
else:
        print('ERROR')