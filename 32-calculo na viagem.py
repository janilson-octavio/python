distancia = float(input("qual a distancia de sua viagem?"))
print("vc está preste a começar uma viagem de {} kz".format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("E o preço de sua viagem é de {:.2f} kz".format(preço))
