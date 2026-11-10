from random import randint
from time import sleep
computador = randint(0, 10)
print("-=-"* 40)
print("Olá, fala o seu computador, vou pensar em um número entre 0 e 10, tente adivinhar!")
print("-=-"* 40)
while True:
    nome = str(input("Como devo chamar-te?: "))
    jogador = int(input("em qui número eu pensei, {}?: ".format(nome)))
    print("processando...")
    sleep(3)
    if jogador == computador:
        print("parabens, vc conseguiu adivinhar!")
    else:
         print("errado, eu pensei no número {} não {},tente de novo! ".format(computador,jogador))
         resp = str(input("Quer continuar? [S/N]"))
         if  resp.upper() == "N":
             break
print()
print("-="*39)
print("FIM DO PROGRAMA!")
print("=-"*39)