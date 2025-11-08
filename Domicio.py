#Pedidio domicilio 
 
#Variables iniciales 
tengo_hambre=True 
tengo_dinero=True 

#Verificar si se puede hacer el pedido 
if tengo_hambre and tengo_dinero: 
    #Datos del usuario 
    direccion_hogar=input("Ingrese su dirección de entrega: ") 
    app_comida="App comida rápida" 

    print("\nUsando la aplicación:", app_comida) 
    print("Pido comida rápida...") 
    print("Doy la dirección al repartidor:", direccion_hogar) 
    print("Recibido el pedido.") 
    print("Pago el pedido") 

    #Preguntar si desea dar propina 
    propina=input("¿Desea dar propina al repartidor? (Si/no): ").lower() #Convierte lo que el usuario a minúsculas, para evitar errores con "Si" o "SI" 
     
    if propina == "si": 
        print("El repartidor se va agradecido por el servicio") 
    else: 
        print("El repartidor se retira cabizbajo") 

    #Comida terminada 
    print("Termino mi comida") 
    tengo_hambre=False 
    print("Ahora tengo_hambre =", tengo_hambre) 
else: 
    #Si no se cumple la condición incial 
    print("No puedo hacer el pedido, o no tengo hambre o no tengo dinero")