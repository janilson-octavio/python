núm = (int(input("digite um número:")),
       int(input("digite outro número:")),
       int(input("digite mais um número:")),
       int(input("digiteum outro número:")))
print(f"os números inseridos são {núm}")
print(f"o valor 9 foi inserido {núm.count(9)} vezes")
if 3 in núm:
    print(f"o número  3 se enconta na posição {núm.index(3)+1}.ª")
else:
    print("Erro. o número 3 não se encontra no programa!")
print("os valores pares digitados são ", end=",")
for n in núm:
  if n % 2 == 0:
      print(n, end=" ")
