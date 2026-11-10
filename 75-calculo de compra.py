total = totmil = menor = cont = 0
barato = ""
while True:
    produto = str(input("Nome do produto:"))
    preço = float(input(" Quanto custa o preoduto: kz"))
    total += preço
    cont  += 1
    if preço > 1000:
        totmil +=1
    if cont == 1 or  preço < menor:
        menor = preço
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quuer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

print("{:^40}".format("FIM DO PROGRAMA"))
print(f"total das compra é {total:.2f}kz")
print(f"temos {totmil} produtos custando mais de mil kz ")
print(f"O menor produto é {menor}")
print(f"O  produto  mais barato é o(a)-{barato}")


