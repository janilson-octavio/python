from datetime import date
atual = date.today().year
nascimento = int(input("ano de nascimento:"))
idade = atual - nascimento
print(" o atleta tem {} anos".format(idade))
if idade <=9 :
    print("classificador:  MIRIM")
elif idade <= 14:
    print("classificador : INFANTIL")
elif idade <= 19:
    print("classificador: JUNIOR")
elif idade <= 25:
    print("classificador: SéNIOR")
else:
    print("classificador: MASTER")
