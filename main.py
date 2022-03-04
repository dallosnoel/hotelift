class Lift:
    def __init__(self, sor):
        s = sor.strip().split(" ")
        self.datum = s[0]
        self.sorszam = s[1]
        self.indulo = s[2]
        self.erkezo = s[3]

lista = []
with open("lift.txt") as f:
    for sor in f:
        lista.append(Lift(sor))
        
#3. feladat
print(f"3. feladat: Összes lifthasználat: {len(lista)}")

#4. feladat
for sor in lista:
    ido1 = max(lista, key=lambda x:x.datum).datum
    ido2 = min(lista, key=lambda x:x.datum).datum
print(f"4. feladat: Időszak: {ido2[:-1]} - {ido1[:-1]}")

#5. feladat
for sor in lista:
    legnagyobb = max(lista, key=lambda x:x.erkezo).erkezo
print(f"5. feladat: Célszint max: {legnagyobb}")

#6. feladat
print(f"6. feladat: ")
kartya_szam = input("Kártya száma: ")
celszint_szam = input("Célszint száma: ")

#7. feladat
for sor in lista:
    if kartya_szam == sor.sorszam:
        if celszint_szam == sor.erkezo:
            print(f"7. feladat: A(z) {kartya_szam}. kártyával utaztak a(z) {celszint_szam}. emeletre")
            break
    if kartya_szam == sor.sorszam:
        if celszint_szam != sor.erkezo:
            print(f"7. feladat: A(z) {kartya_szam}. kártyával nem utaztak a(z) {celszint_szam}. emeletre")
            break

#8. feladat
stat = dict()
for sor in lista:
    stat[sor.datum] = stat.get(sor.datum, 0) + 1
    
print("8. feladat: Statisztika ")
for kulcs, ertek in stat.items():
    print(f"       {kulcs[:-1]} - {ertek}x")
