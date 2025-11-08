#Gimnasio_Motivación+bono 
dias= int(input("¿Cuántos días entrenaste esta semana?: ")) 
puntos=0 
  
#Evaluar la cantidad de días
if dias >= 4: 
    print("¡Excelente disciplina!") 
    puntos += 1 #Suma 1 punto de energía.Significa aumentar en 1 (Es una forma abreviada de escribir puntos=puntos + 1)
elif dias >= 2: 
    print("Bien, pero puedes dar más") 
else: 
    print("Ey que pasa, tú puedes mejorar") 

#Mostrar los puntos si ganó  alguno 
if puntos >  0: 
    print("Has ganado", puntos, " puntos de energía.")