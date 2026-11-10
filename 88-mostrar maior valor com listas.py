listanum = []
mai = 0
men = 0
for p in range(0,5):
    listanum.append(int(input(f"digite um número para  posição {p}: ")))
    if p == 0:
        mai = men = listanum[p]
    else:
        if  listanum[p] > mai:
            mai = listanum[p]
        if listanum[p] < men:
            men = listanum[p]
print("=-" *30)
print(f"os valores da lista são {listanum}")
print(f"O maior valor digitado foi  {mai} na posição! ", end="")
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi  {men} na posição! ", end="")
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}...",end="")
print()
print("=_"*30)
print("FIM DA AULA, VOLTE SEMPRE ORUCH!")