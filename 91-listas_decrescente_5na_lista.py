valores = list()
while True:
    valores.append(int(input("digite um número: ")))
    resp = str(input('Quer continuar [S/n]: '))
    if resp in "Nn":
        break
print("=-"*30)
print(f"eu digitei {len(valores)} elementos!")
valores.sort(reverse=True)
print(f"os valores em ordem decrescente apresentam-se assim {(valores)} ")
if 5 not in valores:
        print("O número 5 não se encontra na lista!")
else:
        print("número 5 encontrado com sucesso!")
