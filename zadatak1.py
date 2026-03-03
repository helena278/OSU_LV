workHours = float(input("Unesite broj radnih sati:"))
hourPrice = float(input("Unesite iznos po radnom satu"))



def totalEuro(workHours,hourPrice):
    return workHours*hourPrice

print(f"Ukupno: {totalEuro(workHours,hourPrice)} eura")