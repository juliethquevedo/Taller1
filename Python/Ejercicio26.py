tipo_cliente = int(input("Ingrese tipo de cliente (1=VIP, 2=Normal): "))
compra = float(input("Ingrese valor de la compra: "))

if tipo_cliente == 1:

    descuento = compra * 0.20
    total = compra - descuento

    print("Cliente VIP")
    print("Descuento:", descuento)
    print("Total a pagar:", total)

elif tipo_cliente == 2:

    descuento = compra * 0.05
    total = compra - descuento

    print("Cliente Normal")
    print("Descuento:", descuento)
    print("Total a pagar:", total)

else:
    print("Tipo de cliente invalido")