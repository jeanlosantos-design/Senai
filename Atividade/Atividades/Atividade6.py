peso = float(input("Peso do prato (0 para sair): "))

while peso != 0:
    total = peso * 12
    print("Total a pagar: R$", total)
    
    peso = float(input("Peso do prato (0 para sair): "))