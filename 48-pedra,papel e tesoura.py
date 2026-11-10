from random import randint
from time import sleep
itens = ("pedra", "papel", "tesoura")
computador = randint(0,2)
print(''' suas opções:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input("qual é a sua jogada:"))
print("jo")
sleep(1)
print("ken")
sleep(1)
print("po!!!")
print("-="*20)
print("computador jogou {} ".format(itens[computador]))
print("jagador jogou {}".format(itens[jogador]))
print("-="*20)
if computador ==0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE!")

    elif jogador == 2:
        print("COMPUTADOR VENCE!")
    else:
        print("JOGADA INVALIDA!")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print(" EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCE!")
    else:
        print("JOGADA INVALIDA!")
elif  computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE!")
    elif jogador == 1 :
        print("COMPUTADOR VENCE!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVALIDA!")









