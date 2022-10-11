'''
#bucle while

i=0

bandera = True

while (bandera == True):
    print("No hagas esto nunca",i)
    i = i+1
    if (i == 30000):
        bandera = False
print ("Terminado")
'''


'''
#Tabla de multiplicar de un número

from re import I


num = 0
i = 0
bandera = True

num = int (input("Dime un número: \n"))

while (i<=10):

    print (num, "*", i, "=", num*i)
    i=i+1
'''

#Contraseña

contra = "Paca34"
incorrecta = ""


while (incorrecta != contra):

    incorrecta = input("¿Cuál es la contraseña?: \n")
    
if (incorrecta == contra):

    print("Felicidades, has entrado")

      