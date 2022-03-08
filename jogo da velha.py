tabuleiro = [["-","-","-"],
                     ["-","-","-"],
                     ["-","-","-"]]
def printar(tabuleiro):
    for i in range(len(tabuleiro)):
        print(tabuleiro[i])

jogador1 = str(input())
jogador2 = str(input())
simbolo1 = str(input())
simbolo2 = str(input())
fim = False


while fim != True:
    #entrada da coordenada
    jogada_player_1 = tuple(input())
    tabuleiro[jogada_player_1(0)][jogada_player_1(1)]
    #igualdade

    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo1:
            fim = True
            ganhador = jogador1
        elif tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo1:
            fim = True
            ganhador = jogador1
        elif tabuleiro[i][i] == tabuleiro[i][i] == tabuleiro[i][i] == simbolo1:
            fim = True
            ganhador = jogador1
    jogada_player_2 = tuple(input())
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo2:
            fim = True
            ganhador = jogador1
        elif tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo2:
            fim = True
            ganhador = jogador2
    printar(tabuleiro)

