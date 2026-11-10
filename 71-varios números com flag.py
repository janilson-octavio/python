soma = cont = 0
while True:
    num = int(input("digite um valor, (000 para parar):"))
    if num == 000:
        break
    soma += num
    cont += 1
print(f"A soma dos {cont} valores é igual a {soma}")

