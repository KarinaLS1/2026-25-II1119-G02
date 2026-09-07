#Declaración
carnet_acceso: int
supervisor_presiona_botón: bool 
puerta_electrónica: bool
#Entradas
carnet_acceso = 20
supervisor_presiona_botón = False
#Proceso
puerta_electrónica = (carnet_acceso < 50) or supervisor_presiona_botón
#Salida
if puerta_electrónica:
    print("abriendo puerta")
else:
    print("apertura de puerta negada")
