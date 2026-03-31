'''Zadatak 4.5.1 Skripta zadatak_1.py ucitava podatkovni skup iz data_C02_emission.csv.
Potrebno je izgraditi i vrednovati model koji procjenjuje emisiju C02 plinova na temelju ostalih numerickih ulaznih veli ˇ cina. Detalje oko ovog podatkovnog skupa mogu se prona ˇ ci u 3. ´
laboratorijskoj vježbi.'''

import pandas as pd
df = pd.read_csv("data_C02_emission.csv")

'''a) Odaberite željene numericke veličine specificiranjem liste s nazivima stupaca. Podijelite
podatke na skup za ucenje i skup za testiranje u omjeru 80%-20%.'''

from sklearn.model_selection import train_test_split

features = ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", "Fuel Consumption Hwy (L/100km)", "Fuel Consumption Comb (L/100km)"]
target = "CO2 Emissions (g/km)"

X_train, X_test, y_train, y_test = train_test_split(df[features],df[target], test_size=0.2, random_state=1)

'''b) Pomocu matplotlib biblioteke i dijagrama raspršenja prikažite ovisnost emisije C02 plinova ´
o jednoj numerickoj veli ˇ cini. Pri tome podatke koji pripadaju skupu za u ˇ cenje ozna ˇ cite ˇ
plavom bojom, a podatke koji pripadaju skupu za testiranje oznacite crvenom bojom.'''

import matplotlib.pyplot as plt

plt.figure()
plt.scatter(X_train["Engine Size (L)"], y_train, color='blue', label='Trening skup', alpha=0.5)
plt.scatter(X_test["Engine Size (L)"], y_test, color='red', label='Testni skup', alpha=0.5)
plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("Ovisnost emisije CO2 o veličini motora")
plt.show()


'''c) Izvršite standardizaciju ulaznih velicina skupa za u ˇ cenje. Prikažite histogram vrijednosti ˇ
jedne ulazne velicine prije i nakon skaliranja. Na temelju dobivenih parametara skaliranja ˇ
transformirajte ulazne velicine skupa podataka za testiranje'''

from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.hist(X_train["Engine Size (L)"], bins=20, color='blue', alpha=0.7)
plt.title("Prije standardizacije")
plt.subplot(1,2,2)
plt.hist(X_train_n[:,0], bins=20, color='red', alpha=0.7)
plt.title("Poslije standardizacije")
plt.show()

'''d) Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i
povežite ih s izrazom 4.6.'''
import sklearn.linear_model as lm

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)

print("Koeficijent: ", linearModel.coef_)
print("Odsječak na osi y: ", linearModel.intercept_)

'''e) Izvršite procjenu izlazne velicine na temelju ulaznih veli ˇ cina skupa za testiranje. Prikažite ˇ
pomocu dijagrama raspršenja odnos izme ´ du stvarnih vrijednosti izlazne veli ¯ cine i procjene ˇ
dobivene modelom.'''

y_predict = linearModel.predict(X_test_n)
plt.figure(figsize=(10,5))
plt.scatter(y_test, y_predict, color='blue', alpha=0.7)
plt.xlabel("Stvarna vrijednost")
plt.ylabel("Procjena")
plt.title("Odnos između stvarnih vrijednosti izlazne veličine i procjene dobivene modelom")
plt.show()


'''f) Izvršite vrednovanje modela na nacin da izra ˇ cunate vrijednosti regresijskih metrika na ˇ
skupu podataka za testiranje.'''

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

mae = mean_absolute_error(y_test, y_predict)
print("Mean absolute error: ", mae)
mse = mean_squared_error(y_test, y_predict)
print("Mean squared error: ", mse)
r2 = r2_score(y_test, y_predict)
print("R2: ", r2)