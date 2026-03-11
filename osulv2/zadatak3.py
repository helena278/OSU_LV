import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")


if img.ndim == 3:
    img_gray = img[:, :, 0].copy()
else:
    img_gray = img.copy()


is_float = np.issubdtype(img_gray.dtype, np.floating)
max_val = 1.0 if is_float else 255.0

def clip_img(a):
    return np.clip(a, 0, max_val)

# a)
bright = clip_img(img_gray + (0.15 * max_val))

# b)
h, w = img_gray.shape
q = w // 4
second_quarter = img_gray[:, q:2*q]

# c) 
rot_cw = np.rot90(img_gray, k=3)

# d)
mirror = np.fliplr(img_gray)


plt.figure()
plt.imshow(img_gray, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.figure()
plt.imshow(bright, cmap="gray")
plt.title("a) Posvijetljena")
plt.axis("off")

plt.figure()
plt.imshow(second_quarter, cmap="gray")
plt.title("b) Druga cetvrtina po sirini")
plt.axis("off")

plt.figure()
plt.imshow(rot_cw, cmap="gray")
plt.title("c) Rotacija 90° (CW)")
plt.axis("off")

plt.figure()
plt.imshow(mirror, cmap="gray")
plt.title("d) Zrcaljena (L-R)")
plt.axis("off")

plt.show()