menu=12000 #Precio fijo del menú

bebida= input("¿Desea agregar bebida? (si/no): ").lower() #Preguntar si quiere bebida
#Si el cliente quiere bebida, se suma 3000 
if bebida == "si": 
    total= menu + 3000 
else: #Si no quiere bebida solo paga el menú
    total=menu 
iva=total * 0.08 #Calcular el porcentaje del IVA
total_iva= total + iva #Sumar el IVA al total
print("El total a pagar, con IVA incluido es: $", round(total_iva))