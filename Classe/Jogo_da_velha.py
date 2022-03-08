class jogo_da_velha:
    def __int__(self, jogador1, jogador2, figura_jogador1, figura_jogador2,):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.figura_jogador1 = jogador1
        self.figura_jogador2 = jogador2

    def tabuleiro(self):
        self.tabuleiro = [["-","-","-"],
                     ["-","-","-"],
                     ["-","-","-"]]
    def printar(self, tabuleiro):
        print(self.tabuleiro)
    def jogada(self, jogada1, jogada2):
        self.jogada1 = jogada1
        self.jogada2 = jogada2

    #def jogar(self,posição_1, posição_2):
    #    posição_1 =

    #    self.tabuleiro[][]

jogo1 = jogo_da_velha( "Carlos", "isaque")
