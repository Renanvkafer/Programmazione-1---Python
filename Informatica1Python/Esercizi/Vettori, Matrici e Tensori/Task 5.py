"""
Dato il seguente tensore multidimensionale:
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a 3-dimensional tensor (values between -1  and 1)
tensor = np.random.uniform(-1, 1, (3, 5, 2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = tensor.nonzero()
ax.scatter(x, y, z, c=tensor[x, y, z], cmap='viridis')
plt.show()

print("\n", tensor)
print("\n", tensor.shape)


#Esplora il tensore con dei cicli for, stampando solo i valori maggiori di 0
for x in range(tensor.shape[0]):
    for y in range(tensor.shape[1]):
        for z in range(tensor.shape[2]):
            if tensor[x, y, z] < 0:
                print(tensor[x,y,z], end='')

print("\n")

canal2 = tensor[:2, :2 :2]

print("\n", canal2)



