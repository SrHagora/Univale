import numpy as np
dieimes_matriz = np.array ([
    [3,4,1],
    [3,2,1]
])
soma_de_matriz=0

for matriz in dieimes_matriz:
    for numeros in matriz:
        soma_de_matriz += matriz

print("A soma da matriz e",soma_de_matriz)