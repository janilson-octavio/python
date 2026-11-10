'''from math import factorial
n = int(input("digite um número para ver seu factorial:"))
f = factorial(n)
print("O factorial de {} é {}".format(n,f))'''

n = int(input("degite um número:"))
c = n
f = 1
while c > 0:
    print(" {} ".format(n),end=" ")
    print(" x " if c > 1 else " = ",end="")
    f *= c
    c-= 1
print("{}".format(f))


