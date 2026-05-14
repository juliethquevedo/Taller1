nota = float(input("Ingrese nota: "))

if nota >= 4.5 and nota <= 5:
    print("Excelente")

elif nota >= 4 and nota < 4.5:
    print("Bueno")

elif nota >= 3 and nota < 4:
    print("Aprobado")

else:
    print("Reprobado")