player_1 = int(input("Escreva o Valor do Jogador 1 (1: pedra, 2: papel, 3: tesoura, 4: lagarto, 5: Spock): "))
player_2 = int(input("Escreva o Valor do Jogador 2 (1: pedra, 2: papel, 3: tesoura, 4: lagarto, 5: Spock): "))

if (1 <= player_1 <= 5) and (1 <= player_2 <= 5):
    if player_1 == player_2:
        print("EMPATE")
    else:
        if (player_1 == 1 and (player_2 == 3 or player_2 == 4)) or \
           (player_1 == 2 and (player_2 == 1 or player_2 == 5)) or \
           (player_1 == 3 and (player_2 == 2 or player_2 == 4)) or \
           (player_1 == 4 and (player_2 == 2 or player_2 == 5)) or \
           (player_1 == 5 and (player_2 == 1 or player_2 == 3)):
            print("Jogador 1 wins!")
        else:
            print("Jogador 2 wins!")
else:
    print("Entrada inválida. Por favor, escolha um número entre 1 e 5 para representar as opções.")
