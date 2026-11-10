print("-^"* 17)
print("calculo de menoridade e maioridade.")
print("-^"* 17)
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input("em qui ano a {}° pessoa nasceu?".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("-=" * 17)
print("\033[31mao todo tivemos {} pessoas maioridade".format(totmaior))
print("e tanbém tivemos {} pessoas menoridade".format(totmenor))
print("-=" * 17)
