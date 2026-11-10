largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
área = largura * altura
print("sua parede tem a dimensão de {} x {} e a sua area é de {}m²".format(largura, altura, área))
tinta = área / 2
print("vc vai precisar de {} litros de tinta para pintar a parede. ".format(tinta))