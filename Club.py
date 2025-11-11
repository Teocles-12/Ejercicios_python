#Club NOCHE ESTELAR 
#Pedir la edad al usuario 
edad= int(input("Ingrese su edad: ")) 
documento= input("¿Tiene documento? (Si/no): ").lower() # Pedir si tiene documento 
#Validar la edad
if edad < 18: 
    print("Entrada denegada") 
else: #Si tiene 18 o más, revisar si tiene documento
    if documento == "si":  
        print("Puede ingresar al club.") 
    else: 
        print("Debe presentar documento.") 

