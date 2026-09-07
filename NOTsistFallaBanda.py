#Declaraciones 
posible_atasco: bool
caja_detectada: bool
motor_activo: bool
#Entradas
caja_detectada = True
motor_activo = False
#Procesos
posible_atasco = caja_detectada and not motor_activo
#Salida
if posible_atasco:
    print("Alerta atasco")