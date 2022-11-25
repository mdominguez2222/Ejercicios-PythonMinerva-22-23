#Funciones definidas por el usuario

def imprimirHola(nombre:str, apellido:str):
    print("Hola", nombre, apellido)

imprimirHola("Juan", "Zamora")


#Crear una función que reciba 2 numeros enteros y los suma

def sumaNumeros(num1:int, num2:int):
    print(f"La suma es {num1+num2}")

sumaNumeros(6,7)

#Return devuelve variables

def sumaNumeros(num1:int, num2:int):   
    return num1+num2 

suma = sumaNumeros(6,7)
print ("La suma es:", suma)