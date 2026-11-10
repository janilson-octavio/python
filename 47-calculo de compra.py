print("{:=^40}".format(" store darkoruch "))
preço = float(input("preço das compras: kz"))
print('''formas de pagamento
[1] A vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input("qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print("sua compra será parcelada em 2x  de {}kz sem juros".format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("quantas parcelas? "))
    parcela = total / totparc
    print("sua compra será parcelada em 2x de {} com juros".format(totparc,parcela))
else:
    total = 0
    print("opção invalida de pagamento. tente novamente!")
print("sua compra de {}kz, vai custar {}kz no final".format(preço,total))
