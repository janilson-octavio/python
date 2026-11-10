listagem = ("celular",169.000,
            "auricular",1000,
            "computador",350.000,
            "mouse",4500,
            "HDD",28.000,)
print("-"*40)
print(f'{"listagem de preços"}:^20')
print("-"*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"{listagem[pos]:>7.2f}")
print("-"*20)




