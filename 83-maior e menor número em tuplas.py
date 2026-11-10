from random import randint
números = (randint(1,10),
           randint(1,10),
           randint(1,10),
           randint(1,10))
print(f"os números qui eu sorteei são {números}. ")
for n in números:
    print("",end="")
print(f" os menores números são {min(números)}")
print(f" os maiores números são {max(números)}",)
