toth18 = toth = totm20 = totm = 0
while True:
    idade = int(input("Idade:"))
    sexo = " "
    while sexo not in "F/M":
      sexo = str(input("sexo:[M/F]")).strip().upper()
    if idade >= 18:
        toth18 +=1
    if sexo == "M":
        toth +=1
    if sexo == "F" and idade > 20:
        totm20 +=1
        totm += 1
    resp = " "
    while resp not in "SN":
          resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

print(f"total  de homens menores de idade é {toth18}. ")
print(f"total de homens  cadastrados é {toth} e de mulheres é {totm} .")
print(f"total de mulheres  maenores  de 20 é {totm20}.")







