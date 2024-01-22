from random import randint
from time import sleep

choice = int(input('''
                    0[Par]
                    1[Impar]'''))
itens = ('Par', 'Impar')
player = int(input('choice a number 0 ~ 100 '))
print('wait for computer choice')
sleep(3)
computer = randint(0,100)
s1 = (player + computer) % 2

print('your choice {}'.format(itens[choice]))
print('you choice a number {}'.format(player))
print('computer choice a number {}'.format(computer))

if choice == 0:
    if s1 == 0:
        print('YOU WIN')
    else:
        print('YOU LOSE')
elif choice == 1:
    if s1 == 0:
        print('YOU LOSE')
    else:
        print('YOU WIN')
else:
        print('ERROR')
