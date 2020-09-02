import config as conf
from DISClib.ADT import map as map
from DISClib.DataStructures import listiterator
from DISClib.ADT import list as lst

#Crear map/dictionary

def comp(key, elem):
    return key == elem

comidas = map.newMap(12007, maptype='PROBING', comparefunction=comp)

#                comida,    tipo
map.put(comidas, "manzana", "fruta")
map.put(comidas, "banano", "fruta")
map.put(comidas, "lechuga", "verdura")
map.put(comidas, "espinaca", "verdura")
map.put(comidas, "almendra", "nuez")

#========================================
# Quiero saber cuales son las comidas de cada tipo
#========================================
