#Solicitar al usuario la cantidad de panes que desea comprar 
cantidad= int(input("Ingrese la cantidad de panes que desea comprar: ")) 
 
#Verificar si la cantidad ingresada es válida 
if cantidad < 0: #Esto evita que el usuario ingrese números negativos y se da a entender que si el número es menor a cero nos muestre el mensaje
    print("Cantidad inválida") 
else: #Si la cantidad NO ES NEGATIVA 
    #Precio por unidad de pan 
    Precio_pan=300 
      
    #Calcular el precio total sin descuento 
    total=cantidad * Precio_pan #se multiplica la cantidad de panes por el precio del pan, dandonos el total sin descuento

    if cantidad > 50: 
        descuento= 0.20 #20% de descuento, Si la compra es mayor a 50 panes 
    elif cantidad > 20: 
        descuento= 0.10 #10 de descuento, y si la compra es mayor a 20 panes
    else: 
        descuento=0.0 # Sin descuento, Si compra 20 o menos panes 

    #Calcular el total con descuento
    total_final=total - (total * descuento) #Se calcula el valor final restando el porcentaje del descuento al total

    #Mostar el resultado final 
    print("Total a pagar: $", total_final)
