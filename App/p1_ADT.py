import config as conf
from DISClib.ADT import map as map
from DISClib.DataStructures import listiterator

#Crear map/dictionary

def comp(key, elem):
    return key == elem

comidas = map.newMap(12007, maptype='PROBING', comparefunction=comp)

#agregar valores, PUT
map.put(comidas, "manzana", "fruta")
map.put(comidas, "banano", "fruta")
map.put(comidas, "lechuga", "verdura")
map.put(comidas, "espinaca", "verdura")
map.put(comidas, "almendra", "nuez")

#Buscar un valor, GET
print(map.get(comidas, "manzana")["value"])

print()

# #Recorrer todas las llaves, KEYS
keys = map.keySet(comidas)
i = listiterator.newIterator(keys)
while listiterator.hasNext(i):
    k = listiterator.next(i)
    print(k)


print()

# #Recorrer las llaves y los valores
keys = map.keySet(comidas)
i = listiterator.newIterator(keys)
while listiterator.hasNext(i):
    k = listiterator.next(i)
    v = map.get(comidas, k)["value"]
    print(k, v)

# #Remplazar un valor, PUT
map.put(comidas, "espinaca", "comida verde")

# #Eliminar un valor, DELETE
# del comidas["espinaca"]
map.remove(comidas, "espinaca")

print()