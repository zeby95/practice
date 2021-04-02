with open('eredmenyek.csv','r', encoding='ISO-8859-1') as adatok:
    adatok.readline()
    matrix = [sor.strip().split(';') for sor in adatok]
#3. feladat:
hazai = 0
idegen = 0
for sor in matrix:
    hazai += sor[0].count('Real Madrid')
    idegen += sor[1].count('Real Madrid')

print(f"3. feladat: Real Madrid Hazai: {hazai}, Idegen: {idegen}")
#4. feladat:
real = []
for sor in matrix:
    hazaiP = int(sor[2])
    idegenP = int(sor[3])
    if sor[0] == 'Real Madrid' or sor[1] == 'Real Madrid':
        real.append([hazaiP,idegenP])

if hazaiP == idegenP:
    print(f"4. feladat: Volt döntetlen? igen")
else:
    print(f"4. feladat: Volt döntetlen? nem")
#5 feladat:
for sor in matrix:
    if sor[0].__contains__('Barcelona'):
        nev = sor[0]

print(f"5. feladat: A barcelonai csapat neve: {nev}")
#6. feladat:
print(f"6. feladat:")
for sor in matrix:
    hazaiCs = sor[0]
    idegenCs = sor[1]
    hazaiP = int(sor[2])
    idegenP = int(sor[3])
    datum = sor[5]
    if datum == '2004-11-21':
        print(f"\t{hazaiCs}-{idegenCs} ({hazaiP}:{idegenP})")
#7. feladat:
adat = dict()
db = 0
for sor in matrix:
    stadion = sor[4]
    adat[stadion] = adat.get(stadion, 0) + 1
print(f"7. feladat:")
for stadion, db in adat.items():
    if db > 20:
        print(f"\t{stadion}: {db}")



        

   

         
