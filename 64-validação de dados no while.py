sexo = str(input("informe seu sexo [M/f]:")).strip().upper()[0]
while sexo not in "[MnFf]":
    sexo = str(input("erro de dados. informe novamente se sexo [M/f]:")).strip().upper()[0]
print("sexo {} registado com sucesso!".format(sexo))
