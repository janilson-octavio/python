números =list()
while True:
    N = int(input("Digite um número:"))
    if N not in números:
        números.append(N)
        print("valor adicionado com sucesso!")
    else:
        print("Valor duplicado, Não vou adicionar!")
    R = str(input("Quer continuar? [S/N]"))
    if R not in "Ss":
      print("Erro, tente novamente!")
    if R in "Nn":
        break

print("=-"* 30)
números.sort()
print(f"OS valores digitados foram {números}!")
print("=-"* 30)