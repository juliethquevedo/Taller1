compra = float(input("Ingresar el valor de la compra:"))
if compra >= 100000:
    descuento= compra*0.10
    total=compra-descuento
    print("Descuento:",descuento)
    print("Total a pagar:",total)
else:
    print("No tiene descuento")
print("Total a pagar:",total)
    
    