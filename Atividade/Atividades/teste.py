distancia = 100

print("=== SENSOR DE ESTACIONAMENTO ===")

while distancia >= 0:
    
    print("\nDistância do muro:", distancia, "cm")
    
    if distancia > 50:
        print("🔊 BIP!")
        
    elif distancia > 10:
        print("🔊🔊 BIP! BIP!")
        
    elif distancia > 0:
        print("🚨 BIP BIP BIP (PERIGO)")
        
    else:
        print("💥 COLISÃO 💥")
    
    distancia = distancia - 10

print("\nSistema encerrado.")-