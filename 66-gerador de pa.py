print("GERADOR DE PEA")
print("-="*20)
primeiro = int(input(" primeiro termo:"))
razão = int(input("razão da PA:"))
termo = primeiro
cont = 1
while cont <= 10:
    print("{}->".format(termo), end="")
    termo += razão
    cont += 1
print("fim.")



