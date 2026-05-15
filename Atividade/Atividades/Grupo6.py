# Sensor de Estacionamento
# Grupo 6

# Mensagem de boas-vindas
print("=== SENSOR DE ESTACIONAMENTO ===")
print("Integrantes: Júlio, Nome2, Nome3")

# Solicita a distância inicial do obstáculo
distancia = int(input("Digite a distância inicial do obstáculo (cm): "))

print("\nIniciando sensor...\n")

# Laço de repetição para simular a aproximação do veículo
while distancia >= 0:

    # Estrutura condicional para definir os avisos sonoros
    if distancia > 30:
        print(f"Distância: {distancia} cm -> BIP...")

    elif distancia > 10 and distancia <= 30:
        print(f"Distância: {distancia} cm -> BIP BIP (Cuidado)")

    # ALERTA MÁXIMO quando chegar em 10 cm
    elif distancia == 10:
        print(f"Distância: {distancia} cm -> ⚠ ALERTA MÁXIMO ⚠")
        print("BIP BIP BIP BIP (FREAR IMEDIATAMENTE)")

    else:
        print(f"Distância: {distancia} cm -> BIP BIP BIP (PERIGO DE COLISÃO)")

    # Verifica se ocorreu colisão
    if distancia == 0:
        print("\nColisão detectada!")
        break

    # Decrementa a distância de 10 em 10 cm
    distancia -= 10

    # Evita que a distância fique negativa
    if distancia < 0:
        distancia = 0