num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input("digite um númmero:")))
    resp = str(input("Quer contiunar? [S/N]: "))
    if resp in "Nn":
        break
for i, n in enumerate(num):
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        ímpares.append(n)
print(f"lista de pares {pares} !")
print(f"lista de ímpares {ímpares}")