print("gerador de PA")
print("-="*10)
primeiro = int(input("primeiro termo:"))
razão =  int(input("razão da PA"))
termo = primeiro
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print("{}->".format(termo), end="")
        termo += razão
        cont += 1
    print("pausa!")
    mais = int(input("quantos termos vc quer aumentar?"))
print("progressão finalizada com {} termos".format(tot))




