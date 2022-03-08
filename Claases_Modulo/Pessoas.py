from datetime import datetime

class pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) #Variavel da classe

class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False, andar = False, parar = False, jogar = False, beber = False):
         self.nome = nome
         self.idade = idade
         self.comendo = comendo
         self.falando = falando
         self.andar = andar
         self.parar = parar
         self.jogar = jogar
         self.beber = beber
    def comer(self, alimento):
        if self.comendo:
          print(f"{self.nome} ja esta comendo.")
          return
        if self.falando:
          print(f"{self.nome} não pode comer pois esta falando.")
          return
     #codigo a ser executado caso não entre nos condicionais

        print(f"{self.nome} esta comendo {alimento}.")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo")
            return
        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} ele não pode falar comendo.")
            return
        if self.falando:
            print(f"{self.nome} ja esta falando sobre {self.assunto}.")
            return
        print(f"{self.nome} esta falando sobre {self.assunto}.")
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.falando} não esta falando.")

        print(f"{self.nome} parou de falar.")
        self.falando=False

    def beber(self, bebida):


        print(f"{self.nome} esta bebendo {self.bebida}")
        self.bebendo = True
    def get_ano_nascimento(self):
        
        idade = self.ano_atual - self.idade
        return print(f"o ano de nascimento é {idade}" )
