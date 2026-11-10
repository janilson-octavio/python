print("-="*20)
print("EQUêNCIA DE FIBONACCI")
print("-="*20)
t = int(input("quantos termos vc quer mostrar?"))
t1 = 0
t2 = 1
print("~"*20)
print("{}->{}".format(t1,t2), end="")
cont = 3
while cont <= t:
    t3 = t1 + t2
    print("{}->".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print("fim!")
print("~"*20)



