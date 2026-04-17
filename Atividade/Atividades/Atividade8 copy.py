dia = int(input("Dia: "))
mes = int(input("Mês: "))

dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

total = dia + sum(dias_mes[:mes-1])

print("Dias desde o início do ano:", total)