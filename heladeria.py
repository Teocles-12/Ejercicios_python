#pedir al usuario que elija un sabor 
sabor= input("Ingresa el sabor de helado (Chocolate o vainilla): ").lower() 
 
#Definir los precios base 
precio=0 

if sabor == "chocolate": 
    precio=4000 
elif sabor == "vainilla": 
    precio=3500 
else: 
    print("Sabor no disponible.") 
    exit() #Si el sabor no existe, detenemos el programa con 'exit()'. con esa funcion el programa termina ahi mismo sin seguir con las demas lineas 
       
#Preguntar si quiere topping       
topping= input("¿Desea topping? (Si/no): ").lower() 
 
#Si el usuario quiere topping, sumar 1000 al precio
if topping == "si" or topping == "Si": 
    precio += 1000  
#Mostar el valor de todo    
print("El total a pagar es: $", precio) 
