núm = int(input("digite um número:"))
tot = 0
for c in range(1, núm + 1):
    if núm % c ==0:
        print("\033[33m ", end="")
        tot +=1
    else:
        print("\033[31m", end="")
    print("{} ".format(c), end="")
print("\033[m o número {} foi divisivel {} vezes".format(núm,tot))
if tot ==2:
    print("por isso ele é primo!")
else:
    print("por isso ele não é primo!")

