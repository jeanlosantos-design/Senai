dia = int(input("Dia: "))
mes = int(input("Mês: "))

dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

if mes < 1 or mes > 12:
    print("Mês inválido!")
elif dia < 1 or dia > dias_mes[mes-1]:
    print("Dia inválido!")
else:
    total = dia + sum(dias_mes[:mes-1])
    print("Dias:", total)