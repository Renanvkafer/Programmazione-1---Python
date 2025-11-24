"""
Data un'immagine ed una maschera binaria come le seguenti:

Stampa le dimensioni della maschera e dell'immagine. Sono uguali? In caso contrario porta la maschera ad avere le stesse dimensioni dell'immagine e moltiplicale. Suggerimento: usa la funzione np.expand_dims

Usa lo slicing per estrarre solo la porzione centrale dell'immagine risultante

"""

import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("Lenna.png")[...,::-1]

mask = (cv2.imread("Lenna_face_mask.png", 0)/255).astype(np.uint8)


plt.imshow(img),plt.figure()
plt.imshow(mask),plt.figure()

print("immagine: ")
print(img)

print("maschera: ")
print(mask)

print("img_shape:",img.shape,"\nmask_shape:",mask.shape)

mask = np.expand_dims(mask, axis=2)
print("img_shape:",img.shape,"\nmask_shape:",mask.shape)


select_face = img * mask
print("selected_face",select_face.shape)


cv2.imshow("Imagem", img)
cv2.imshow("Máscara", mask)
cv2.imshow("Select Face", select_face)
cv2.waitKey(0)
cv2.destroyAllWindows()


a, b = img.shape[:2]

h_offset = a // 4
w_offset = b // 4
centro = img[h_offset : -h_offset, w_offset : -w_offset]


cv2.imshow("Centro", centro)
cv2.waitKey(0)
cv2.destroyAllWindows()





