import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()




K = 5  

kmeans = KMeans(n_clusters=K, random_state=42)
labels = kmeans.fit_predict(img_array)
centers = kmeans.cluster_centers_

# zamijeni RGB vrijednosti svakog piksela s najbližim centrom
img_array_aprox = centers[labels]

# transformiraj natrag u dimenzije originalne slike
img_aprox = np.reshape(img_array_aprox, (w, h, d))

# prikaz kvantizirane slike
plt.figure()
plt.title(f'Kvantizirana slika - K={K}')
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()

# ---- Inertia / J ovisnost o broju grupa ----
J_values = []
K_values = range(1, 11)
for k in K_values:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(img_array)
    J_values.append(km.inertia_)

plt.figure()
plt.plot(K_values, J_values, marker='o')
plt.xlabel("Broj grupa K")
plt.ylabel("Inertia (J)")
plt.title("Ovisnost J o broju grupa K")
plt.grid(True)
plt.show()

# ---- Binarne slike po grupi ----
for k in range(K):
    binary_img = (labels == k).reshape(w, h)  # True/False za grupu k
    plt.figure()
    plt.imshow(binary_img, cmap='gray')
    plt.title(f'Binarna slika - grupa {k}')
    plt.axis('off')
    plt.show()