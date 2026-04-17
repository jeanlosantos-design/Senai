soma = 0
contador = 1

while contador <= 5:
    salario = float(input(f"Digite o salário do {contador} Funcionário: "))
    contador += 1
    soma += salario
    media = soma / 5

print ("A média salarial dos 5 funcionários é: ", media)