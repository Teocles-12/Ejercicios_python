#Precio base del libro 
precio_libro=25000 

#Preguntar si es estudiante 
estudiante=input("¿Eres estudiante? (Si/no): ").lower() 

#Preguntar si tiene cupón
cupon= input("¿Tienes un cupón? (si/no): ").lower() 

#Crear una variable para guardar el total
total=precio_libro

#Si es estudiante, se aplica un descuento del 15 porciento
if estudiante == "si": 
    total=total - (precio_libro * 0.15) 

    #Si además tiene un cupón, se le solicita el código
    if cupon == "si": 
        codigo= input("Ingresa el código del cupón: ").upper() #Sirve para convertir todas las letras a mayúsculas

        #Si el cupón es correcto, aplica un 10 porciento adicional
        if codigo == "LIBRO10": 
            total= total - (total * 0.10) 
        else: 
            print("Cupón incorrecto, no se aplica descuento adicional.") 

#Si no es estudiante, no se aplica el cupón 
else: 
    if cupon == "si": 
        print("El cupón no aplica porque no eres estudiante.") 

print("El total a pagar es: $", round(total))
