import config as conf
from DISClib.ADT import map as map
from DISClib.DataStructures import listiterator
from DISClib.ADT import list as lst

#Crear map/dictionary

def comp(key, elem):
    return key == elem

animales = map.newMap(12007, maptype='PROBING', comparefunction=comp)

#                id,
map.put(animales, "1", {"tipo": "ave", "num_pies": 2, "nombre": "colibri"})
map.put(animales, "2", {"tipo": "insecto", "num_pies": 6, "nombre": "mariposa"})
map.put(animales, "3", {"tipo": "mamifero", "num_pies": 4, "nombre": "perro"})
map.put(animales, "4", {"tipo": "mamifero", "num_pies": 0, "nombre": "ballena"})
map.put(animales, "5", {"tipo": "ave", "num_pies": 2, "nombre": "avestrus"})

#========================================
# Quiero buscar los animales por tipo y num_pies
#========================================
