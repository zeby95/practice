#7.feladat ismétlődés kiszámítása
def ismetlodo(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
#7.feladat----------------------------------------------------------------
with open('pilotak.csv', 'r', encoding='utf-8') as adatok:
    adatok.readline()
    matrix = [sor.strip().split(';') for sor in adatok]
#3.feladat:
print('3. feladat: ',len(matrix))
#4.feladat:
lastItem = matrix[-1][0]
print('4. feladat: ', lastItem)
#5.feladat:
print('5. feladat:\t ')
for sor in matrix:
    if int(sor[1][:4]) < 1901:
        nev = sor[0]
        szulDatum = sor[1]
        print(f"\t {nev} ({szulDatum}.)")
#6.feladat:
lista = []
for sor in matrix:
    if  sor[3] != '':
        szam = int(sor[3])
        lista.append(szam)
        legkisebb = lista[0] if lista else None
        for i in lista:
            if i < legkisebb:
                legkisebb = i
for sor in matrix:
     if  sor[3] != '':
         if int(sor[3]) == legkisebb:
              nemzet = sor[2]       
print('6. feladat:',nemzet)    
#7.feladat:
lista = []
for sor in matrix:
    if  sor[3] != '':
        szam = int(sor[3])
        lista.append(szam)
        
eredmeny = str(ismetlodo(lista))[1:-1]
print('7. feladat:',eredmeny)
