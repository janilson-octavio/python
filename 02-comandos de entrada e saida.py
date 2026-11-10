nome = input("informe seu nome:")
sexo = input("informe seu sexo:")
if sexo == "m":
  print("olá, seja bemvindo, {}! ".format(nome,sexo))
elif sexo == "f":
    print("olá, seja bemvinda, {}! ".format(nome,sexo))
else:
    print("erro na execusão de dados, por favor tente mais tarde! ")
