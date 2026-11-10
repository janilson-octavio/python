resp ="S"
soma = média = quant = maior = menor = 0
while resp in "Ss":
    núm = int(input("digite um número:"))
    soma += núm
    quant+=1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input("quer continuar? [S/N]")).upper().strip()[0]
média = soma /quant
print("vc digitou {}  número e a média é {}".format(quant,média))
print("maior número foi {} e o menor é {}".format(maior,menor))


