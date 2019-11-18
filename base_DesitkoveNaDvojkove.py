print("Napište desítkové číslo pro převedení na dvojkové: ",end="")

neco = True
binarniCislo = []
i = 0

while neco == True:
    try:
        cislo = int(input())
        neco = False
    except:
        neco = True

cisloVys = cislo
rozdil = cislo % 2

while cisloVys > 0:
    binarniCislo.append(rozdil)
    cisloVys = cisloVys // 2
    rozdil = cisloVys % 2


binarniCislo.reverse()


for x in binarniCislo:
    if x == 1:
        x = x-1
        print(binarniCislo[x],end = "")

    else:
        x = x + 1
        print(binarniCislo[x],end = "")


    
