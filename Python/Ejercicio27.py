mes = int(input("Ingrese numero del mes (1-12): "))

if mes == 12 or mes == 1 or mes == 2:
    print("Invierno")

elif mes >= 3 and mes <= 5:
    print("Primavera")

elif mes >= 6 and mes <= 8:
    print("Verano")

elif mes >= 9 and mes <= 11:
    print("Otoño")

else:
    print("Mes invalido")