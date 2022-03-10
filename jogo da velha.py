tabuleiro = [["-","-","-"],
                     ["-","-","-"],
                     ["-","-","-"]]
def printar(tabuleiro):
    for i in range(len(tabuleiro)):
        print(tabuleiro[i])

jogador1 = str(input("Insira o nome do primeiro jogador: "))
jogador2 = str(input("Insira o nome do segundo jogador: "))
simbolo1 = str(input("Escolha entre X ou O: "))
if simbolo1 == "X":
    simbolo2 = "O"
else:
    simbolo2 = "X"


fim = False


while fim != True:
    #entrada da coordenada
    jogada_player_1_x = int(input())
    jogada_player_1_y = int(input())
    tabuleiro[jogada_player_1_x][jogada_player_1_y] = simbolo1

    #igualdade
    #Varrer as linhas , colunas e diagonais em busca do padrão do jogador 1
    printar(tabuleiro)
    for i in range(3):
        #linhas
        if tabuleiro[i][0] == simbolo1 and tabuleiro[i][1] == simbolo1 and tabuleiro[i][2] == simbolo1:
            fim = True
            ganhador = jogador1
        #colunas
        elif tabuleiro[0][i] == simbolo1 and tabuleiro[1][i] == simbolo1 and tabuleiro[2][i] == simbolo1:
            fim = True
            ganhador = jogador1
        #diagonal 1
        elif tabuleiro[i][i] == simbolo1 and tabuleiro[i][i] == simbolo1 and tabuleiro[i][i] == simbolo1:
            fim = True
            ganhador = jogador1

    jogada_player_2_x = int(input())
    jogada_player_2_y = int(input())
    tabuleiro[jogada_player_2_x][jogada_player_2_y] = simbolo2
    #igualdade
    #Varrer as linhas , colunas e diagonais em busca do padrão do jogador 2

    for i in range(3):
        if (tabuleiro[i][0] == simbolo2) and (tabuleiro[i][1] == simbolo2) and (tabuleiro[i][2] == simbolo2):
            fim = True
            ganhador = jogador2
        elif (tabuleiro[0][i] == simbolo2) and (tabuleiro[1][i] == simbolo2) and (tabuleiro[2][i] == simbolo2):
            fim = True
            ganhador = jogador2
        elif (tabuleiro[i][i] == simbolo2) and (tabuleiro[i][i] == simbolo2) and (tabuleiro[i][i] == simbolo2):
            fim = True
            ganhador = jogador2

    printar(tabuleiro)

print(ganhador)


