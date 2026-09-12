#Declaración 
nivel_líquido: float
válvula_drenaje: bool
encender_bomba: bool

#Entradas 
nivel_líquido = 0
válvula_drenaje = False

#Proceso
encender_bomba = nivel_líquido <1 and not válvula_drenaje

#Salida
if encender_bomba:
    print("encender bomba")
else:
    print("no encender bomba")