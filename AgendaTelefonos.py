'''
Opción 1:
Lista para nombres
Lista para telefonos

Opción 2:
Lista para nombres y telefonos
Ejemplo [Juan-Telefono, Pepe-Telefono]
'''

#Opción 1:

vNombres = []
vTelefonos = []

nombre = input("Dime un nombre: \n")
telefono = input("Dime un teléfono: \n")

vNombres.append(nombre)
vTelefonos.append(telefono)

vNombres.append("Mario")
vTelefonos.append("234")

print (vNombres)
print (vTelefonos)
