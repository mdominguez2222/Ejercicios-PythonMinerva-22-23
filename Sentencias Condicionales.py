#Sentencias condicionales

#1-Leer tu edad por teclado e imprima por pantalla si eres mayor de edad o menor

edad = 0

edad = (int) (input("Dime tu edad:\n"))   #input siempre me devuelve stream(str), asi que tenemos que definir que es entero(int)

if (edad>=18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
