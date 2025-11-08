#Puntos 5 y 6 
    #Pago y descuentos  

    #Suponiendo que ya tengo los datos del usuario
type_bicycle= "Estándar" 
bedrock_cost= 3000 #Valor total sin descuento
time=75 #tiempo de uso
 
#Pidiendo el método de pago
payment_method= input("Método de pago (efectivo / tarjeta / puntos): ").lower() #'.lower()' Convierte la entrada en minúsculas
  
    #Variables para guardar descuentos, recargos o penalización 
discount=0 
surcharge=0 
penalty=0
 
    #Aplicando condiciones según los requerimientos 

        #Si el usuario usa la bicicleta más de 60 minutos y paga con tarjeta
if time > 60 and payment_method == "tarjeta": 
    discount= bedrock_cost * 0.10 
    print("Descuento del 10 porciento aplicado por uso prolongado y pago con tarjeta.")   
    
    #Si el uso es menor a 10 minutos y paga con puntos no hay descuento
elif time < 10 and payment_method == "puntos": 
    print("No hay descuento por uso corto con puntos") 
     
     #Si es fin de semana, se aplica un recargo del 5%
day= input("¿Es fin de semana? (Si/no): ").lower() 
if day == "si" or day == "Si": 
    surcharge= bedrock_cost * 0.05 
    print("Recargo del 5 porciento aplicado por fin de semana.") 
 
    #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower() 
if out_time == "si" or out_time == "Si":
    penalty=2000 
    print("Penalización fija de $2000 aplicada por retraso.") 
 
    #Calculando el total
total= bedrock_cost - discount + surcharge + penalty 
 
    #Mostrando el resumen 
print("\n--- RESUMEN PAGO ---") 
print("Tipo de bicicleta:", type_bicycle) 
print("Timepo de uso:", time, "minutos") 
print("método de pago:", payment_method.capitalize()) #'.capitalize' lo usamos para poner mayúsculas la primera letra del texto (Se usa con cadenas de texto(String)) y dejar las demás en minúscula.
print("Precio base: $", bedrock_cost) 
print("Descuento: $", discount) 
print("Recargo: $", surcharge) 
print("Penalización: $", penalty) 
print("--------------------------") #No hace nada solo hace que se vea bonito y ya
print("Total a pagar: $", round(total,2)) #'round()' lo usamos para formatear o redondear números decimales a las cifras que se indique.