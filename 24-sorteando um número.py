#num = int(input("informe um número:"))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print("a unidade: {}".format(u))
#print("a dezena: {}".format(d))
#print("a centena: {}".format(c))
#print("o milhar: {}".format(m))

num = int(input("informe um número:"))
n = str(num)
print("analisando o número {}".format(num))
print("unidade: {}".format(n[3]))
print("dezena: {}".format(n[2]))
print("centena: {}".format(n[1]))
print("milhar: {}".format(n[0]))