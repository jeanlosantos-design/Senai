numero = int(input("Digite o número para ver a tabuada: "))

for contador in range(0, 11):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
