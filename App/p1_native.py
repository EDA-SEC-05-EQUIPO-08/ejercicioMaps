#Crear map/dictionary
comidas = {}

#agregar valores, PUT
comidas["manzana"] = "fruta" 
comidas["banano"] = "fruta" 
comidas["lechuga"] = "verdura" 
comidas["espinaca"] = "verdura" 
comidas["almendra"] = "nuez" 


#Buscar un valor, GET
print(comidas["manzana"])

print()

#Recorrer todas las llaves, KEYS
for k in comidas.keys():
    print(k)

print()

#Recorrer las llaves y los valores
for k, v in comidas.items():
    print(k, v)

#Remplazar un valor, PUT
comidas["espinaca"] = "comida verde" 

#Eliminar un valor, DELETE
del comidas["espinaca"]

print()
print(comidas)