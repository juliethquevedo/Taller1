edad=int(input("Ingrese su edad:"))
if edad>=0 and edad<=12:
    print("Es niño")

elif edad>=13 and edad<=17:
    print("Es joven")

elif edad>=18 and edad<=59:
    print("Es adulto")

else:
    print("Es adulto mayor")
