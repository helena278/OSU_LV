'''Zadatak 3.4.1 Skripta zadatak_1.py ucitava podatkovni skup iz ˇ data_C02_emission.csv.
Dodajte programski kod u skriptu pomocu kojeg možete odgovoriti na sljede ´ ca pitanja:'''

import pandas as pd
data = pd.read_csv("lv3/data_C02_emission.csv")

'''a) Koliko mjerenja sadrži DataFrame? Kojeg je tipa svaka velicina? Postoje li izostale ili ˇ
duplicirane vrijednosti? Obrišite ih ako postoje. Kategoricke veli ˇ cine konvertirajte u tip ˇ
category.'''

print("broj mjerenje: ", len(data))
print("\ntipovi podataka: ", data.dtypes)
print("\nizostale vrijednosti: ", data.isnull().sum())
print("\nduplicirane vrijednosit: ", data.duplicated().sum())

data = data.dropna()
data = data.drop_duplicates()

categorical_cols = ["Make", "Model", "Vehicle Class", "Transmission", "Fuel Type"]

for col in categorical_cols:
    data[col] = data[col].astype("category")

'''b) Koja tri automobila ima najvecu odnosno najmanju gradsku potrošnju? Ispišite u terminal: ´
ime proizvoda¯ ca, model vozila i kolika je gradska potrošnja.'''

most_consuming = data.nlargest(3, 'Fuel Consumption City (L/100km)')
least_consuming = data.nsmallest(3, 'Fuel Consumption City (L/100km)')

print("Najmanje gradska potrošnja: ")
print(least_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print("Najveća gradska potrošnja: ")
print(most_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

'''c) Koliko vozila ima velicinu motora izme ˇ du 2.5 i 3.5 L? Kolika je prosje ¯ cna C02 emisija ˇ
plinova za ova vozila?'''

selected_data = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
print(f"Broj vozila s motorom između 2.5 i 3.5 L: , {len(selected_data)}")
print(f"Prosječna emisija CO2 za ta vozila: {selected_data['CO2 Emissions (g/km)'].mean()} g/km")

'''d) Koliko mjerenja se odnosi na vozila proizvoda¯ ca Audi? Kolika je prosje ˇ cna emisija C02 ˇ
plinova automobila proizvoda¯ ca Audi koji imaju 4 cilindara?'''
audi_data = data[data['Make'] == 'Audi']
print(f"Broj mjerenja za Audi: {len(audi_data)}")

audi_4cyl = audi_data[audi_data['Cylinders'] == 4]
print(f"Prosječna emisija CO2 za AUdi s 4 cilindra: {audi_4cyl['CO2 Emissions (g/km)'].mean()} g/km")

'''e) Koliko je vozila s 4,6,8. . . cilindara? Kolika je prosjecna emisija C02 plinova s obzirom na ˇ
broj cilindara?'''

cylinder_counts = data['Cylinders'].value_counts().sort_index()
print("Broj vozila po broju cilindara: ")
print(cylinder_counts)

cylinder_emission = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
print("Prosječna emisija Co2 po broju cilindara: ")
print(cylinder_emission)

'''f) Kolika je prosjecna gradska potrošnja u slu ˇ caju vozila koja koriste dizel, a kolika za vozila ˇ
koja koriste regularni benzin? Koliko iznose medijalne vrijednosti?'''
diesel_vehicles = data[data['Fuel Type'] == 'D']
gasoline_vehicles = data[data['Fuel Type'].isin(['Z', 'X'])]

print("Dizel:")
print(f"Prosječna potrošnja: {diesel_vehicles['Fuel Consumption City (L/100km)'].mean()} L/100km")
print(f"Medijalna potrošnja: {diesel_vehicles['Fuel Consumption City (L/100km)'].median()} L/100km")

print("Benzin:")
print(f"Prosječna potrošnja: {gasoline_vehicles['Fuel Consumption City (L/100km)'].mean()} L/100km")
print(f"Medijalna potrošnja: {gasoline_vehicles['Fuel Consumption City (L/100km)'].median()} L/100km")

'''g) Koje vozilo s 4 cilindra koje koristi dizelski motor ima najvecu gradsku potrošnju goriva? '''
most_consuming_diesel_4cyl = diesel_vehicles[diesel_vehicles['Cylinders'] == 4].nlargest(1, 'Fuel Consumption City (L/100km)')
print("Najveća gradska potrošnja za 4-cilindrično dizel vozilo:")
print(most_consuming_diesel_4cyl[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

'''h) Koliko ima vozila ima rucni tip mjenja ˇ ca (bez obzira na broj brzina)?'''

manual_vehicles = data[data['Transmission'].str.startswith('M', na=False)]
print(f"Broj vozila s ručnim mjenjačem: {len(manual_vehicles)}")

'''i) Izracunajte korelaciju izme ˇ du numeri ¯ ckih veli ˇ cina. Komentirajte dobiveni rezultat.'''

correlation_matrix = data.corr(numeric_only=True)
print("Korelacija između numeričkih veličina:")
print(correlation_matrix)


