from datetime import datetime

class pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) #Variavel da classe

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        self.variavel = "Valor"

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return
        if self.falando:
            print(f"{self.nome} não pode comer pois esta falando.")
            return

        print(f'{self.nome} esta comendo {alimento}.')
        self.comendo = True
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo.")
            return
        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} ele não pode falar comendo")
            return
        if self.falando:
            print(f"{self.nome} ja esta falando.")
            return

        print(f'{self.nome} esta falando sobre {assunto}. ')
        self.falando = True
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando.')
            return

        print(f"{self.nome} parou de falar.")
        self.falando = False
    def get_ano_nascimento(self):
        
        idade = self.ano_atual - self.idade
        return print(f"o ano de nascimento é {idade}" )
