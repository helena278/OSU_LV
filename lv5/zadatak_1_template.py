import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#Skripta zadatak_1.py generira umjetni binarni klasifikacijski problem s dvije
#ulazne velicine. Podaci su podijeljeni na skup za ucenje i skup za testiranje modela.


#a)Prikažite podatke za ucenje u x1−x2 ravnini matplotlib biblioteke pri cemu podatke obojite
#s obzirom na klasu. Prikažite i podatke iz skupa za testiranje, ali za njih koristite drugi
#marker (npr. ’x’). Koristite funkciju scatter koja osim podataka prima i parametre c i
#cmap kojima je moguce definirati boju svake klase.

plt.figure()

# Train
plt.scatter(X_train[:, 0], X_train[:, 1],
            c=y_train, cmap='bwr', marker='o', label='Train')

# Test
plt.scatter(X_test[:, 0], X_test[:, 1],
            c=y_test, cmap='bwr', marker='x', label='Test')

plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title('Train i test podaci')
plt.show()

#b)Izgradite model logisticke regresije pomocu scikit-learn biblioteke na temelju skupa podataka
#za ucenje.
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

#c)

theta0 = model.intercept_[0]
theta1 = model.coef_[0][0]
theta2 = model.coef_[0][1]

print("theta0:", theta0)
print("theta1:", theta1)
print("theta2:", theta2)

plt.figure()

# Podaci
plt.scatter(X_train[:, 0], X_train[:, 1],
            c=y_train, cmap='bwr', marker='o')

# Granica odluke
x1_vals = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
x2_vals = -(theta0 + theta1 * x1_vals) / theta2

plt.plot(x1_vals, x2_vals, 'k-', label='Granica odluke')

plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title('Granica odluke')
plt.show()

#d)Provedite klasifikaciju skupa podataka za testiranje pomocu izgradenog modela logisticke
#regresije. Izracunajte i prikažite matricu zabune na testnim podacima. Izracunate tocnost,
#preciznost i odziv na skupu podataka za testiranje.


from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

y_pred = model.predict(X_test)

# Matrica zabune
cm = confusion_matrix(y_test, y_pred)
print("Matrica zabune:\n", cm)

# Metrike
print("Točnost:", accuracy_score(y_test, y_pred))
print("Preciznost:", precision_score(y_test, y_pred))
print("Odziv:", recall_score(y_test, y_pred))

#e)Prikažite skup za testiranje u ravnini x1−x2. Zelenom bojom oznacite dobro klasificirane
#primjere dok pogrešno klasificirane primjere oznacite crnom bojom.

plt.figure()

correct = (y_test == y_pred)
incorrect = (y_test != y_pred)

# Točni
plt.scatter(X_test[correct, 0], X_test[correct, 1],
            c='green', marker='o', label='Točno')

# Pogrešni
plt.scatter(X_test[incorrect, 0], X_test[incorrect, 1],
            c='black', marker='x', label='Pogrešno')

plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title('Rezultati klasifikacije')
plt.show()