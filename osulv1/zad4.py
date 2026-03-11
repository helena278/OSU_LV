brojanje_rijeci={}

with open("song.txt") as datoteka:
    for linija in datoteka:
        linija=linija.strip()
        rijeci=linija.split()

        for rijec in rijeci:

            rijec.lower()

            if rijec in brojanje_rijeci:
                brojanje_rijeci[rijec]+=1
            else:
                brojanje_rijeci[rijec]=1

rijeci_jednom=[]

for kljuc, vrijednost in brojanje_rijeci.items():
    if vrijednost==1:
        rijeci_jednom.append(kljuc)
    
print(len(rijeci_jednom))
print(rijeci_jednom)

