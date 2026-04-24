
quantidade = int(input("Digite a quantidade de sanduíches: "))


queijo_kg = (quantidade * 100) / 1000

presunto_kg = (quantidade * 50) / 1000


carne_kg = (quantidade * 100) / 10
print("Para fazer", quantidade, "sanduíches, você precisa de:")
print(queijo_kg, "kg de queijo")
print(presunto_kg, "kg de presunto")
print(carne_kg, "kg de carne")