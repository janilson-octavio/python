soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 ==0:
        soma +=1
        cont +=c
print("a soma entre todos os {} valores é igual a {}".format(soma,cont))
