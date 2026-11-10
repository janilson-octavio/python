velocidade = float(input("qual é a velocidade atual do carro!"))
if velocidade > 80:
    print("vc excedeu o limite permitido qui é 80 km/h ")
    multa = (velocidade-80)*7
    print("vc deve pagar uma multa de {:.2f}".format(multa))
print("tenha um bom dia! dirija com cuidado!")