brojevi=[]

while True:
    x=input()

    if x=="Done":
        break

    try:
        broj=int(x)
        brojevi.append(broj)
    except:
        print("Pogrešan unos")
    
    

print("Koliko je brojeva u listi: ", len(brojevi))
print("Srednja vrijednost: ", sum(brojevi)/len(brojevi))
print("Minimalna vrijednost: ", min(brojevi))
print("Maksimalna vrijednost: ", max(brojevi))