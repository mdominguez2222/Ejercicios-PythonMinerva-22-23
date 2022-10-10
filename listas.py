#Listas en python, almacenan datos del mismo y distinto tipo
#Definición e inicialización

vNombres = []  #Corchetes para tipo lista

#Insertar un dato
vNombres.insert(0,"Juan")    #insert necesita 2 argumentos, inserta en la posición que le digas
vNombres.insert(1,"Pepe")
vNombres.insert(2,"Inés")  
vNombres.append("Minerva")   #append lo pone al final de la lista
vNombres.insert(1,"Julian")  #si hay dos en la misma pocición lo desplaza

#Eliminar elementos
#vNombres.clear()    Borra toda la lista

vNombres.remove("Pepe")   #Elimina a quien le digamos de la lista 

print(f"Elnombre borrado es {vNombres.pop(1)}")  #pop saca un valor pero lo guarda


#Ordenar una lista

vNombres.sort(reverse=True)   #Con reverse puedo ordenar de mayor a menor(inverso)


#Contar los elementos de la lista

print (f"Inés aparece", vNombres.count("Inés"), "veces")
print ("La lista tiene", len(vNombres))  #len lee todos los elementos


print (vNombres)