lista = [1,5,25,100,500]

print("Inicial", lista)
#
lista.append(250)
print("Append: ",lista)
#
lista2 =  [75,125]
lista.extend(lista2)
print("Extend: ",lista)
#
lista.insert(9,400)
print("Insert: ",lista)
#
lista.remove(400)
print("Remove: ", lista)