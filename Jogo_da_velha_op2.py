def printar(tabuleiro):
    for i in range(len(tabuleiro)):
        print(tabuleiro[i])
def jogo_da_velha():
    tabuleiro = [["-", "-", "-"],
                 ["-", "-", "-"],
                 ["-", "-", "-"]]
    jogador1 = str(input("Insira o nome do primeiro jogador: "))
    jogador2 = str(input("Insira o nome do segundo jogador: "))
    simbolo1 = str(input("Escolha entre X ou O: "))
    if simbolo1 == "X":
        simbolo2 = "O"
    else:
        simbolo2 = "X"

    fim = False
    laço_checar_espaço_preenchido = False
    acu = 0
    while fim != True:


        # não alocar jogada em espaço que ja foi preenchido
        while laço_checar_espaço_preenchido == False:
            # entrada da coordenada
            jogada_player_1_x = int(input(f"Para a jogada '{simbolo1}'' digite a coordenada x: "))
            jogada_player_1_y = int(input(f"Para a jogada '{simbolo1}' digite a coordenada y: "))
            print(jogada_player_1_x, jogada_player_1_y)

            if tabuleiro[jogada_player_1_x][jogada_player_1_y] != simbolo1 and tabuleiro[jogada_player_1_x][jogada_player_1_y] != simbolo2:
                laço_checar_espaço_preenchido = True
                tabuleiro[jogada_player_1_x][jogada_player_1_y] = simbolo1
            if laço_checar_espaço_preenchido == False:
                print(f"Por favor outra coordenada, pois {jogada_player_1_x,jogada_player_1_y} ja esta preenchida")
        laço_checar_espaço_preenchido = False
        printar(tabuleiro)
        # igualdade
        # Varrer as linhas , colunas e diagonal (esquerda pra direita) em busca do padrão do jogador 1
        for i in range(3):
            # Coração do jogo, o condicional if de comparação
            if ((tabuleiro[i][0] == simbolo1) and (tabuleiro[i][1] == simbolo1) and (tabuleiro[i][2] == simbolo1)) or (
                    (tabuleiro[0][i] == simbolo1) and (tabuleiro[1][i] == simbolo1) and (tabuleiro[2][i] == simbolo1)) or (
                    (tabuleiro[0][0] == simbolo1) and (tabuleiro[1][1] == simbolo1) and (tabuleiro[2][2] == simbolo1)):
                fim = True
                ganhador = jogador1
        #Diagonal (direita para esquerda)

        if (tabuleiro[0][2] == simbolo1) and (tabuleiro[1][1] == simbolo1) and (tabuleiro[2][0] == simbolo1):
            fim = True
            ganhador = jogador1

        while laço_checar_espaço_preenchido == False:
            # entrada da coordenada
            jogada_player_2_x = int(input(f"Para a jogada '{simbolo2}' digite a coordenada x: "))
            jogada_player_2_y = int(input(f"Para a jogada '{simbolo2}'' digite a coordenada y: "))

            # Coração do jogo, o condicional if de comparação
            if tabuleiro[jogada_player_2_x][jogada_player_2_y] != simbolo1 and tabuleiro[jogada_player_2_x][jogada_player_2_y] != simbolo2:
                laço_checar_espaço_preenchido = True
                tabuleiro[jogada_player_2_x][jogada_player_2_y] = simbolo2
            if laço_checar_espaço_preenchido == False:
                print(f"Por favor outra coordenada, pois {jogada_player_2_x,jogada_player_2_y} ja esta preenchida")
        laço_checar_espaço_preenchido = False
        # igualdade
        # Varrer as linhas , colunas e diagonais em busca do padrão do jogador 2

        for i in range(3):
            if (tabuleiro[i][0] == simbolo2) and (tabuleiro[i][1] == simbolo2) and (tabuleiro[i][2] == simbolo2) or (
                    tabuleiro[0][i] == simbolo2) and (tabuleiro[1][i] == simbolo2) and (tabuleiro[2][i] == simbolo2) or (
                    tabuleiro[0][0] == simbolo2) and (tabuleiro[1][1] == simbolo2) and (tabuleiro[2][2] == simbolo2):
                fim = True
                ganhador = jogador2
            if (tabuleiro[0][2] == simbolo2) and (tabuleiro[1][1] == simbolo2) and (tabuleiro[2][0] == simbolo2):
                fim = True
                ganhador = jogador2
        printar(tabuleiro)
        if acu == 9:
            fim = True
    print(ganhador)

jogo_da_velha()
