from random import shuffle
n1 = str(input("1 nome:"))
n2 = str(input("2 nome:"))
n3 = str(input("3 nome:"))
n4 =str(input("quarto name:"))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("a apresentação da lista será!")
print(lista)