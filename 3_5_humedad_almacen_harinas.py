#declaración 
humedad: float
temperatura: float
falla_seguridad: bool
encender_deshumidificador: bool

#entradas
humedad = 70
temperatura = 30
falla_seguridad = True

#proceso
encender_deshumidificador = (humedad > 60 and temperatura > 20) or not falla_seguridad

#salida
if encender_deshumidificador:
    print("encender deshumidificador")