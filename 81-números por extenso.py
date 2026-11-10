cont = ("zero","um","dois",
        "trés","quatro","cinco",
        "seis","sete","oito",
        "nove","dez","onze",
        "doze","tereze","quatorze"
        ,"quinze","dezaseis","dezasete"
        ,"dezoito","dezanove","vinte")
while True:
    núm = int(input("digite um número entre 0 e 20:"))
    if 0<= núm <= 20:
        break
    print("erro.tente novamente!")
print(f"vc digitou o número {cont[núm]}")
