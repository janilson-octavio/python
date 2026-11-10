from time import sleep
n1 = int(input("digite o primeiro número:"))
n2 = int(input("digite o segundo número:"))
opção = 0
while n1 != 5:
      print('''opções:
      [1] somar
      [2] multiplicar
      [3] maior número
      [4] novos números
      [5] sair do programa''')
      opção = int(input(">>>> qual é a sua opção?"))
      if opção == 1:
          soma = n1 + n2
          print("A soma entre {} + {} = {} ".format(n1,n2,soma))

      elif opção == 2:
          multiplicar = n1 * n2
          print("A multiplicção entre {} * {} = {}".format(n1,n2,multiplicar))

      elif opção == 3:
          if n1 > n2:
             maior = n1
          else:
             maior = n2
          print("o maior número entre {} e {} é {}".format(n1,n2,maior))
      elif opção == 4:
          print("informe novamente os números!")
          n1 = int(input(" primiro número: "))
          n2 = int(input(" segundo número:"))
      elif opção == 5:
          print("finalizando...")

else:
    print("opção invalida. tente novamente!")
    print("-="* 20)
    sleep(2)
print("fim do programa. volte sempre!")



