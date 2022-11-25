'''
Opción 1:
Lista para nombres
Lista para telefonos

Opción 2:
Lista para nombres y telefonos
Ejemplo [Juan-Telefono, Pepe-Telefono]
'''

#Opción 1:

#Creamos el menú de la agenda
'''
1-Insertar contacto
2-Borrar contacto
3-Buscar contacto
4-Ver todos los contactos
5-Salir

'''

#Función que pinta el Menú y devuelve la opción seleccionada del 1 al 5

def pintaMenu():
    opc = 0
    while (opc < 1 or opc > 5):
        print("********Menú agenda********* \n")
        print("1-Insertar contacto")
        print("2-Borrar contacto")
        print("3-Buscar contacto")
        print("4-Ver todos los contactos")    
        print("5-Salir")
        print("****************************")
        
        try:
            opc = int(input("Elige una opción: \n"))
        except:
            print("Las opciones son del 1 al 5")

    return opc


opc = pintaMenu()
while (opc!=5):
    opc = pintaMenu()