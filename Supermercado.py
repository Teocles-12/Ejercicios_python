#Descuentos por cantidad y envío 
#Precio de cada producto 
precio_Unitario=2000 
unidades= int(input("Ingrese la cantidad de productos: "))  
#Aplicar descuentos seún la cantidad
if unidades < 0: 
    print("Error: la cantidad no puede ser negativa.") 
else: 
    total= unidades * precio_Unitario 

    if unidades >= 30: 
        total= total - (total * 0.15) #Descuento del 15 porciento
    elif unidades >= 10: 
        total= total - (total * 0.05) #Descuento del 5 porciento
    #Si el total es menor que 50.000, se agrega costo de envío
    if total < 50000: 
        total= total + 5000 
    print("El total a pagar es: $", round(total))