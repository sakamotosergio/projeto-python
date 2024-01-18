from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
print('''escolha:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')

computador = randint(0,2)
jogador = int(input('faça sua jogada '))

print('escolha do computador {}'.format(itens[computador]))
print('escolha do jogador {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('VOCÊ GANHOU')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATOU')
else:
    print('não pode fazer isso otario')