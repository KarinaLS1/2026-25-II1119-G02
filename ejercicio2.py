#Declaración
presionar_botón_derecho: bool
presionar_botón_izquierdo: bool 
bajar_prensa: bool
#Entradas
presionar_botón_derecho = True
presionar_botón_izquierdo = False
#Proceso
bajar_prensa = presionar_botón_derecho and presionar_botón_izquierdo
#Salida
if presionar_botón_derecho and presionar_botón_izquierdo:
    print("prensa bajando")
else:
    print("presione ambos botones") 

