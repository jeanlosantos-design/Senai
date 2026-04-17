nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input(" "))

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
    print("Notas inválidas!")
else:
    media = (n1*1 + n2*2 + n3*3) / 6
    print("Média:", media)