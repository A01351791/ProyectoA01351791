#En esta parte se analizaran los sostos de la comida
carne_roja = 700
camarones = 400
carne_blanca = 250
pescado = 350

#sacamos la cantidad de dinero que va a gasatr 
dinero_carne_roja= int(input("introduzca el número de días que planea cocinar carne roja al mes "))
dinero_camarones= int(input("introduca el número de días que planea cocinar camarones al mes "))
dinero_carne_blanca= int(input("intoduzca el número de días que planea cocinar carne blanca al mes "))
dinero_pescado= int(input("introduzca el número de días que planea cocianr pescado al mes "))

res= ((carne_roja*dinero_carne_roja)+(camarones*dinero_camarones)+(carne_blanca*dinero_carne_blanca)+(pescado*dinero_pescado))
print("El dinero que vas a gastar al mes de tus comidas es ")
print(res)
#Scamos la cantidad de dinero por semana
dinero_por_semana= (res/4)
print("El dinero que vas a gastar por semana de tus comidas es ")
print(dinero_por_semana)

#preguntamos el dinero que tiene para gastar 
dinero= int(input("introduzca la cantidad de dinero a gastar "))
proceso=  (dinero-res)
print("tu saldo es")
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

numero_de_consumidores = int(input("número de personas "))
print(tipo_de_carne(numero_de_consumidores))

#Este es un ejemplo de el tiempo que se le pregunta al cocinero para prepara carneblanca
def tiempo(minu):
    if minu<= 30:
        return "pechugas de pollo con arroz"
    elif minu>=31 and minu <=60:
        return "alitas de pollo"
    elif minu>=60 and minu <=70:
        return "Tinga de pollo"
    elif minu>=70 and minu <=80:
        return "Enchiladas verdes de pollo"
    else:
        minu = "Pollo con mole"
    return minu
tiempot = float(input("Tiempo para cocinar"))
print(tiempo(tiempot))


