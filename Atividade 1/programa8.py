nome = input("digite seu nome: ")idade = int(input("digite sua idade: "))
idade = int(input("digite sua idade"))
while True:
    idade = int(input("digite sua idade"))
    if idade > 120 or idade < 0:
    print("idade invalida! por favor, digite um valor menor ou igual a 120.")
    else:
        break
            


dias_de_vida = idade * 365  
print("você já viveu:",dias_de_vida, "de sua vida")