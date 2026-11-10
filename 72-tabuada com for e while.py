while True:
    n = int(input("com qual número vc quer ver a tabuada?"))
    if n < 0:
        break
    print("_"*30)
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
    print("_"*30)
print(" programa encerrado!")






