salario=float(input("Salario base:"))
horas=float(input("Horas extra:"))
valorHora=float(input("Valor Hora:"))
extra=horas*(1.5*valorHora)
total=salario+extra
print("Salario total:", total)