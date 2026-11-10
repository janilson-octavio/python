soma= 0
count = 0
for c in range(1,7):
    num = int(input("digite o {}° valor:" .format(c)))
    if num % 2 == 0:
        soma += num
        count += 1
print("vc informou  {} números pares e a soma é {}".format(count,soma))

