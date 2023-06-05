import numpy as np


lista = [1,2,3,4,5]
arreglo = np.array(lista)
print(arreglo)

#ndim indica cuantas dimensiones posee el arreglo
print(f"el arreglo es de :{arreglo.ndim} dimension")

#len indicia el largo que posee
print(f"El arreglo es de largo:{len(arreglo)}")

#slice 
#Star:Stop:Step indica cuando quiere mostrar el arreglo
#Star indica de donde vamos a consultar
#Stop indica hasta donde vamos a consultar
#Step indica cuanto en cuanto vamos a consultar
print(arreglo[::2])

#Rellenar arreglo
#for
lista2 = [i for i in range(1,11)]
arreglo2 = np.array(lista2)
print(arreglo2)

#arange(Star:Stop:Step) rellena el arreglo con valores segun indica
arreglo3 = np.arange(1,11)
print(arreglo3)

#Operaciones
#Sumar
arreglo3 +=5
print(arreglo3)
#multiplicar
arreglo3*=10
print(arreglo3)

#comparaciones o operadores relaciones
print(arreglo3>arreglo2)

#sum() Entrega la suma de los valores del arreglo
print(arreglo3.sum())

#mean Entrega el promedio de valores del arreglo
print(arreglo3.mean())

#max Muestra el valor mas alto
#min Muestra el valor mas bajo
print(f"Numero mas alto {arreglo3.max()}")
print(f"Numero mas bajo {arreglo3.min()}")
