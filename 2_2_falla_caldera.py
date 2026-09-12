#Declaración 
flujo_gas: int
llama_detectada: bool 
activar_sist: bool

#Entradas 
flujo_gas = 1
llama_detectada = False

#Proceso
activar_sist = flujo_gas >0 and not llama_detectada

#Salida
if activar_sist:
    print("Activando sistema de ignición")
else:
    print("no activar")
