#declaración 
humedad_suelo: float
es_noche: bool 
riego_manual: bool
activar_riego: bool 

#entradas
humedad_suelo = 0
es_noche = True
riego_manual = True

#proceso
activar_riego = (humedad_suelo <0.5 and es_noche) or riego_manual

#salida
if activar_riego:
    print("activar riego de zonas verdes")