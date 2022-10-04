
from string import punctuation


puntoA = 0
puntoB = 0

puntoA = (int)(input ("¿A cuánto está el punto A?: \n"))
puntoB = (int)(input ("¿A cuánto está el punto B?: \n"))

if (puntoA<0 and puntoB>0):
    print ("Si vas primero al punto A la distancia es de",((puntoA*(-2))+puntoB), "kilómetros")
    print ("Si vas primero al punto B la distancia es de", ((puntoB*2)-puntoA), "kilómetros")
elif (puntoB>puntoA and puntoB>0 and puntoA>0):
    print ("Si vas primero al punto A la distancia es de",(puntoB), "kilómetros")
    print ("Si vas primero al punto B la distancia", (puntoB+puntoA), "kilómetros")
elif (punto)
