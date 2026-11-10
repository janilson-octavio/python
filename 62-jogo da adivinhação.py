from random import randint
computador = randint(0,10)
print("olá sou o seu computador...vou pensar num número de 0 até 10.")
print("vocé consegui adivinhar qual vai ser a jogada?")
acertou = False
palpites = 0
while not acertou:
    print("-=" * 11)
    jogador = int(input("qual é o seu palpite "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("mais qui isso...")
        if jogador > computador:
            print("menos qui isso!")
    print("-=" * 11)
print("para bens acertou!")
print("Acertou com {} tentativas".format(palpites))


