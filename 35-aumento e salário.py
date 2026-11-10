salário = float(input("qual é o salário do funcionário?"))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + ( salário * 10 / 100)
print("o funcionário ganhava {} kz, por trabalho ardúo passa a ganhar  {} kz agora.".format(salário,novo))

