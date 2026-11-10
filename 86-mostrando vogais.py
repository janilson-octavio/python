palavras = ("aprender",
            "programar",
            "dinheiro",
            "biblia",
            "treino",)
for v in palavras:
    print(f"\nNa palavra {v.upper()} temos", end=" ")
    for letra in v:
        if letra.lower() in "aeiou":
            print(letra, end=" ")




