num = cont = soma = 0
num = int(input("digite um número:"))
while num != 699:
    cont+=1
    soma+=num
    num = int(input("digite um número:"))
print("vc informou {} números e a soma é {}".format(cont,soma))
