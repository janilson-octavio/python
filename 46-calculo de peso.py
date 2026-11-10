peso = float(input("imforme seu peso:"))
altura = float(input("imforme sua altura:"))
imc = peso / (altura ** 2)
print("o seu imc é de {:.2f}".format(imc))
if imc  <= 18.5:
    print("vc está ABAIXO do peso normal!")
elif 18.5 <= imc < 25:
    print("PARABÉNS, vocé está na faixa de peso NORMAL")
elif 25 <= imc < 30:
    print("vc está em SOBREPESO")
elif 30 <= imc < 40:
    print("vc está em OBESIDADE, cuidado!")
elif imc >= 40:
    print("vc está em OBESIDADE MÓRBIDA, muito cuidado!")
