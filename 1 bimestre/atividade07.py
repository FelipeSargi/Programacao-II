import numpy as np
dieimes_matriz = np.array([[3,4,1], 
                           [3,2,1]])
soma = 0
for x in range(dieimes_matriz.shape[0]):
    for y in range(dieimes_matriz.shape[1]):
        soma = soma + dieimes_matriz[x][y]
print(soma)