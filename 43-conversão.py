num = int(input("digite um número inteiro:"))
print('''escolha uma das báses para conversãõ:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opção = int(input("sua opção:"))
if opção == 1:
    print("{} convertido para binário é igual a {}".format(num, bin(num)))
elif opção == 2:
    print("{} convertido para octal é igual a {}".format(num, oct(num)))
elif opção == 3:
    print("{} convertido para hexadecimal é igual a {}".format(num, hex(num)))
else:
    print("erro de procedimento!,opção invalida. tente novamente!")