import numpy as np

lista = [[1,2,3],[4,5,6],[7,8,9]]
arreglo = np.array(lista)
print(arreglo)
arr = np.arange(1,101).reshape(10,10)
print(arr)
print(arr[-1][-1])
numero = int(input("Ingrese numero: "))
for y in range(10):
    for x in range(10):
        if arr[y][x]==numero:
            print(arr[y][x])

print(arr)
print(arr[3:6,0:5])

#Para "borrar"
"""numero = int(input("Ingrese numero: "))
   for y in range(10):
        for x in range(10):
            if arr[y][x]==numero:
                arr[y][x]=0 """""
            