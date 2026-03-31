'''Zadatak 4.5.2 Na temelju rješenja prethodnog zadatka izradite model koji koristi i kategoricku ˇ
varijable „Fuel Type“ kao ulaznu velicinu. Pri tome koristite 1-od-K kodiranje kategori ˇ ckih ˇ
velicina. Radi jednostavnosti nemojte skalirati ulazne veli ˇ cine. Komentirajte dobivene rezultate. ˇ
Kolika je maksimalna pogreška u procjeni emisije C02 plinova u g/km? O kojem se modelu
vozila radi?'''

import pandas as pd
df = pd.read_csv("data_C02_emission.csv")

from sklearn.model_selection import train_test_split

features = ["Engine Size (L)", "Cylinders", "Fuel Consumption Comb (L/100km)"]
target = ["Fuel Type"]

