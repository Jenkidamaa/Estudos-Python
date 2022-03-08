class cliente():
    def __init__ (self, nome, email,plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.lista_planos = ["basico","premium"]
        if plano in self.lista_planos:
            self.plano
        else:
            raise Exception("plano invalido")


    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            raise Exception("plano invalido")




    def ver_filme(self,filme):
        lista_filmes = ["A", "B", "C", "D", "E", "F"]
        lista_filmes_basic = ["C", "D"]

        if self.plano == "premium":
            print("Plano Premium Acesso liberado ")
        elif self.plano != "premium" or filme not in lista_filmes_basic:
            print("Acesso Negado para esses filmes no plano basic")
        else:
            print("Plano Basic Acesso liberado")
Cliente1 = cliente("XXXX","XXXX@hotmail.com", "basico")
print(Cliente1.nome)
print(Cliente1.plano)
Cliente1.mudar_plano("premium")
print(Cliente1.plano)
Cliente1.ver_filme("A")
Cliente1.mudar_plano("basico")
Cliente1.ver_filme("A")
