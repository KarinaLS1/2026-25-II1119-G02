#declaración
compra: float 
total_pagar: float
descuento: float
#entradas
compra = float(input("Ingrese el total de compra: "))
#proceso
if compra > 50000:
    descuento = compra * 0.10
    total_pagar = compra - descuento
    print("Descuento: ", descuento)
else:
    total_pagar = compra
#salida
print("Total pagar: ", total_pagar)