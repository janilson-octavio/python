frase = str(input("digite uma frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
print("o iverso de {} é {}!".format(junto, inverso))
if inverso == junto:
    print("temos um palindromo!")
else:
    print("não é um palindromo!")
