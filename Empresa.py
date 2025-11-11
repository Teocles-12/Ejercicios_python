#Empresa TecnoPLUS 
#Evaluación compuesta con validación de notas 

#Pedir las notas al usuario 
tecnica= float(input("Ingrese la nota de la prueba técnica (0.0 a 5.0): ")) 
logica= float(input("Ingrese la nota de la prueba lógica (0.0 a 5.0): ")) 

#Validar que ambas esten dentro del rango permitido 
if (tecnica < 0 or tecnica > 5) or (logica < 0 or logica > 5): 
    print("Error: las notas deben estar entre 0.0 a 5.0") 
else: 
    nota_final= (tecnica * 0.7) + (logica * 0.3) #Calcular la nota final con los porcentajes
    print("Nota final: ", round(nota_final,2)) #Mostrar la nota final con dos decimales
    #Condiciones según la nota final
    if nota_final >= 3: 
        print("Resultado: Aprovado") 
    elif nota_final >= 2: 
        print("Resultado : Revisión") 
    else: 
        print("Resultado: Reprobado")