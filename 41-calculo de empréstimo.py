val_casa = float(input("quanto custa a casa: kz"))
sal_sujeito = float(input("quanto o sujeito ganha: kz"))
anos = int(input("quantos anos de financiamento? "))
prestação = val_casa /(anos * 12)
minímo = sal_sujeito * 30/ 100
print("para pagar uma casa de {}kz em {} anos ".format(val_casa,anos))
print("a prestação será de {:.2f}kz".format(prestação))
if prestação <= minímo:
    print("empréstimo pode ser CONCEDIDO!")
else:
    print("emprestimo NEGADO!")

