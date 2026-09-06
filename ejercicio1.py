#Declaración
prueba_dimensión: bool
prueba_dureza: bool 
pieza_metálica: bool
#Entradas
prueba_dimensión = True  
prueba_dureza = True 
#Proceso
pieza_metálica = prueba_dimensión and prueba_dureza:
#Salidas
if prueba_dimensión and prueba_dureza: 
  print("pieza aprobada") 
else: 
  print("pieza rechazada")
