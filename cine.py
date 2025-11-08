    #Pedimos la edad del cliente 
edad= int(input("Por favor, ingrese su edad: ")) 
 
    #Verificamos si la edad es negativa 
if edad < 0: 
    print("Error: la edad no puede ser negativa.") 
elif edad < 5: #Si tienes menos de 5 años, entra gratis
    print("Entrada gratis") 
elif edad <11: #Si tiene entre 5 y 11 años
    print("El precio de la entrada es $5.000") 
elif edad <= 59: #Si tiene entre 12 y 59 años
    print("El precio de la entrada es 8.000") 
else: #Si tiene 60 años o más
    print("El precio de la entrada es $4.000 (Descuento adulto mayor).")