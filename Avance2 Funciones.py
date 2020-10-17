#En esta parte se analizaran los sostos de la comida
carne_roja = 700
camarones = 400
carne_blanca = 250
pescado = 350

#sacamos la cantidad de dinero que va a gasatr 
dias_carne_roja= int(input("Introduzca el número de días que planea cocinar carne roja al mes: "))
while dias_carne_roja<0 or dias_carne_roja >16:
    print("Has introducido una cantidad no valida, vuelva a introducir una cantidad")
    dias_carne_roja= int(input("Introduzca el número de días que planea cocinar carne roja al mes: "))
    
dias_camarones= int(input("Introduca el número de días que planea cocinar camarones al mes: "))
while dias_camarones<0 or dias_camarones>16:
    print("Has introducido una cantidad no valida, vuelva a introducir una cantidad")
    dias_camarones= int(input("Introduca el número de días que planea cocinar camarones al mes: "))
    
dias_carne_blanca= int(input("Intoduzca el número de días que planea cocinar carne blanca al mes: "))
while dias_carne_blanca <0 or dias_carne_blanca>16:
    print("Has introducido una cantidad no valida, vuelva a introducir una cantidad")
    dias_carne_blanca= int(input("Intoduzca el número de días que planea cocinar carne blanca al mes: "))
    
dias_pescado= int(input("Introduzca el número de días que planea cocianr pescado al mes: "))
while dias_pescado<0 or dias_pescado>16:
    print("Has introducido una cantidad no valida, vuelva a introducir una cantidad")
    dias_pescado= int(input("Introduzca el número de días que planea cocianr pescado al mes: "))

resultado= ((carne_roja*dias_carne_roja)+(camarones*dias_camarones)+(carne_blanca*dias_carne_blanca)+(pescado*dias_pescado))
print("El dinero que vas a gastar al mes de tus comidas es: ")
print(resultado)
#Scamos la cantidad de dinero por semana
dinero_por_semana= (resultado/4)
print("El dinero que vas a gastar por semana de tus comidas es: ")
print(dinero_por_semana)

#preguntamos el dinero que tiene para gastar 
dinero= int(input("Introduzca la cantidad de dinero a gastar: "))
proceso=  (dinero-resultado)
print("Tu saldo es: ")
print(proceso)

#Sacamos el tipo de comida por la cantidad de personas que van a comer

def tipo_de_carne (a):
    if a <=1:
        return "carneblanca"
    elif a >= 2 and a <=3:
        return "camarones"
    elif a >=4 and a <= 5:
        return "pescado"
    else:
         a = "carneroja"
    return a

numero_de_consumidores = int(input("Introduzca el número de personas que van a comer "))
while numero_de_consumidores<0 or numero_de_consumidores>11:
    print(" El número de consumidores que introdujo es muy alto, vuelva a intoducir una cantidad")
    numero_de_consumidores = int(input("Introduzca el número de personas que van comer "))
    
print(tipo_de_carne(numero_de_consumidores))


#Este es un ejemplo de el tiempo que se le pregunta al cocinero para prepara carneblanca
def tiempo(minutos):
    if minutos<= 30:
        return "Pechugas de pollo"
    elif minutos>=31 and minutos <=60:
        return "Alitas de pollo"
    elif minutos>=60 and minutos <=70:
        return "Tinga de pollo"
    elif minutos>=70 and minutos <=80:
        return "Enchiladas verdes de pollo"
    else:
        minutos = "Pollo con mole"
    return minutos

tiempot = float(input("Introduzca el tiempo en minutos que tiene para cocinar  "))
while tiempot<0 or tiempot>360:
    print("El tiempo introducido no es valido, vuelva a introducir una cantidad ")
    tiempot = float(input("Introduzca el tiempo en minutos  que tiene para cocinar "))
print("Hoy puedes cocinar: ")
print(tiempo(tiempot))
"""
Aqui es donde le sugerimos una guarnición al usuario para cocinar.
Aquí tambien utilizamos la biblioteca de python RANDOM para que el programa
pueda escoger una guarnición de la lista para el usuario
"""

import random

def acompañamientos(guarniciones):
    for x in range(0,len(guarniciones)):
        resultado = random.choice(guarniciones)
    return resultado
        

guarniciones =['Arroz rojo', 'Arroz blanco', 'Frijoles', 'Papas fritas', 'Papas horneadas', 'Verduras', 'Ensalada', 'Puré de papa']
print("Puedes acopañar tu platillo con: ")
print(acompañamientos(guarniciones))




