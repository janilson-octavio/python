print("="*30)
print("{:^40}".format("banco pss"))
print("="*40)
saqu =int(input("Quanto vc quer saquar? kz"))
total = saqu
céd = 50
totalcéd = 0
while True:
    if saqu >= céd:
        total -= céd
        totalcéd += 1
    else:
         if totalcéd > 0:
             print(f"total de {totalcéd} cédulas de {céd} ")
         if céd == 50:
             céd = 20
         if céd == 20:
             céd = 10
         if céd == 10:
             céd = 1
         totcéd = 0
         if total == 0:
             break
print("="*40)
print("{:^40}".format("volte sempre ao banco pss!.tenha um bom dia"))


