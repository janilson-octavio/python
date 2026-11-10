from random import randint
v = 0
while True:
    jogador = int(input("qual é a sua jogada?"))
    computador = randint(0,10)
    tot = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo =str(input("par ou impar? [P/I]")).strip().upper()
        print(f"vc jogou {jogador} e o computador {computador} e o total é {tot}", end=" ")
        print("deu par " if tot % 2 == 0 else " deu impar" )
        if tipo == "p":
             if tot % 2 == 0:
                print("vc venceu!")
                v += 1
             else:
                 print("vc perdeu!")
                 break
        elif tipo == "I":
            if tot % 2 == 1:
                print("vc venceu!")
                v +=1
            else:
                print("vc perdeu!")
                break
        print("vamos jogar novamente...")
    print(f"GAME OVER! vc venceu {v} vez(es).")