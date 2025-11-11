#Calcular la tarifa según las horas de uso 

#Pedir las horas al usuario 
horas= int(input("Ingrese la cantidad de horas que estuvo en el parqueadero: ")) 

#Verificar queno sean horas negativas 
if horas < 0: 
    print("Error: las horas no pueden ser negativas.") 
else: 
    #Si las horas son válidas calcular el total 
    #Si las horas son menores o iguales a 5, se cobra 2000 por cada hora
    if horas <= 5: 
        total=horas * 2000 
    #Si son más de 5, se cobra igual + multa fija de 5000
    else: 
        total= (horas * 2000) + 5000 
    print("El valor total a pagar es: ", total)