p = int(input("Qtd camisetas pequenas: "))
m = int(input("Qtd camisetas médias: "))
g = int(input("Qtd camisetas grandes: "))

total = (p * 10) + (m * 12) + (g * 15)

print(f"Total arrecadado: R$ {total:.2f}")