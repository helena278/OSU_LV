'''Zadatak 3.4.2 Napišite programski kod koji ce prikazati sljede ´ ce vizualizacije:'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("lv3/data_C02_emission.csv")

'''a) Pomocu histograma prikažite emisiju C02 plinova. Komentirajte dobiveni prikaz. ´'''

plt.figure(figsize=(8,5))
plt.hist(data['CO2 Emissions (g/km)'], bins=30, color='red', alpha=0.7, edgecolor='black')
plt.title("Histogram emisije CO2")
plt.xlabel("CO2 Emissions (g/km)")
plt.ylabel("Broj vozila")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


'''b) Pomocu dijagrama raspršenja prikažite odnos izme ´ du gradske potrošnje goriva i emisije ¯
C02 plinova. Komentirajte dobiveni prikaz. Kako biste bolje razumjeli odnose izmedu¯
velicina, obojite to ˇ ckice na dijagramu raspršenja s obzirom na tip goriva. ˇ'''
fuel_colors = {'D': 'blue', 'Z': 'red', 'X': 'green', 'E': 'purple', 'N': 'orange'}
plt.figure(figsize=(8,5))
for fuel_type, color in fuel_colors.items():
    subset = data[data['Fuel Type'] == fuel_type]
    plt.scatter(subset['Fuel Consumption City (L/100km)'], subset['CO2 Emissions (g/km)'], label=fuel_type, color=color, alpha=0.5)

plt.title('Odnos gradske potrošnje goriva i emisije CO2')
plt.xlabel('Gradska potrošnja goriva (L/100km)')
plt.ylabel('CO2 Emisija (g/km)')
plt.legend(title='Tip goriva')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


'''c) Pomocu kutijastog dijagrama prikažite razdiobu izvangradske potrošnje s obzirom na tip ´
goriva. Primjecujete li grubu mjernu pogrešku u podacima? ´'''
data.boxplot(column='Fuel Consumption Hwy (L/100km)', by='Fuel Type', grid=False)
plt.title('Razdioba izvangradske potrošnje goriva po tipu goriva')
plt.suptitle('')  
plt.xlabel('Tip goriva')
plt.ylabel('Izvangradska potrošnja goriva (L/100km)')
plt.show()


'''d) Pomocu stup ´ castog dijagrama prikažite broj vozila po tipu goriva. Koristite metodu ˇ
groupby.'''
fuel_counts = data.groupby('Fuel Type').size()
plt.figure(figsize=(6, 5))
fuel_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Broj vozila po tipu goriva')
plt.xlabel('Tip goriva')
plt.ylabel('Broj vozila')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()



'''e) Pomocu stup ´ castog grafa prikažite na istoj slici prosje ˇ cnu C02 emisiju vozila s obzirom na ˇ
broj cilindara.'''
cylinder_emissions = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
plt.figure(figsize=(8, 5))
cylinder_emissions.plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('Prosječna CO2 emisija po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('CO2 Emisija (g/km)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
