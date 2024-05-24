# Atividade de jogo da veia... (melhor bingo)
p1 = int(input("Digite um número: 1 para Pedra; 2 Para papel; 3 para tesoura: "))
p2 = int(input("Digite um número: 1 para Pedra; 2 Para papel; 3 para tesoura: "))

if (1 <= p1 <= 3) and (1 <= p2 <= 3):
    if p1 == p2:
        print("EMPATE")
    else:
        if (p1 == 1 and p2 == 3) or \
                (p1 == 2 and p2 == 1) or \
                (p1 == 3 and p2 == 2):
            print("Jogador 1 Wins.")
        else:
            print("Jogador 2 Wins.")
else:
    print("Numeração Inválida")
