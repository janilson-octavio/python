núm = [[],[]]
valores = 0
for c in range(1,8):
    valores = int(input(f"digite o {c}° valor: "))
    if valores % 2 == 0:
        núm[0].append(valores)
    else:
        núm[1].append(valores)
print("=-"* 30)
núm[0].sort()
núm[1].sort()
print(f"Os valores pares são: {núm[0]}.")
print(f"Os valores impares são: {núm[1]}.")
print(f"=-"*30)

