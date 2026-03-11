import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=",", skiprows=1)


spol = data[:,0] 
visina = data[:,1] 
masa = data[:,2] 

# a) 
print("Broj osoba:", data.shape[0])

# b)
plt.scatter(visina, masa, s=10)
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Visina vs masa")
plt.show()

# c)
plt.scatter(visina[::50], masa[::50], s=20, color="red")
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Svaka 50-ta osoba")
plt.show()

# d)
print("Min visina:", np.min(visina))
print("Max visina:", np.max(visina))
print("Srednja visina:", np.mean(visina)) #prosjek

# e)
muskarci = visina[spol == 1]
zene = visina[spol == 0]

print("\nMuskarci:")
print("broj:", muskarci.size)
print("min:", np.min(muskarci))
print("max:", np.max(muskarci))
print("mean:", np.mean(muskarci))

print("\nZene:")
print("broj:", zene.size)
print("min:", np.min(zene))
print("max:", np.max(zene))
print("mean:", np.mean(zene))