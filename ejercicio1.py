#Declaración
prueba_dimensión:boolean 
prueba_dureza:boolean 
pieza_metálica:boolean  
#Entradas
prueba_dimensión = true 
prueba_dureza = true 
pieza_metálica = prueba_dimensión + prueba_dureza
#Salidas
if prueba_dimensión AND prueba_dureza
print("pieza aprobada") 
else 
print("pieza rechazada")
