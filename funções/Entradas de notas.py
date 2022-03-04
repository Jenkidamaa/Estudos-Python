#Armazena os nomes juntos com as notas dos alunos em ordem
def armazena(n): #n = numero de alunos
    lista_nome = []
    lista_notas = []
    acu = 1
    while acu <= n:
        lista_nome.append(str(input("Digite o nome do aluno de Ra de numero {}: ".format(acu))))
        n1 = float(input("Digite a primeira nota "))
        n2 = float(input("Digite a segunda nota "))
        lista_notas.append([n1,n2])
        acu += 1
    return lista_nome, lista_notas


#Armazena apenas os nomes dos alunos
def armazena_nome(n): # = numero de alunos
    lista_nome = []
    acu = 1
    while acu <= n:
        lista_nome.append(str(input("Digite o nome do aluno de Ra de numero {}: ".format(acu))))
        acu += 1
    return lista_nome

#Armazena apenas as notas 
def armazena_notas(n,lista):
    lista_notas = []
    acu = 0
    while acu < n:
        print("Insira a nota do aluno {} ".format(lista[acu])) #para esclarecer chama o nome do aluno 
        n1 = float(input("Digite a primeira nota "))
        n2 = float(input("Digite a segunda nota "))        
        lista_notas.append([n1,n2])
        acu += 1
    return lista_notas   
    
# função para tratar os dados calculando as medias, mediana e o desvio padrão das notas da turma
# ∑: símbolo de somatório. Indica que temos que somar todos os termos, desde a primeira posição (i=1) até a posição n
# xi: valor na posição i no conjunto de dados
# MA: média aritmética dos dados
# n: quantidade de dados

def media(lista):
    lista_media = []
    for i in range(len(lista_media)):
        lista_media.append(lista[i][0]+lista[i][1]) #n1+n2
    return lista_media

def mediana(lista):
    lista_organizada = sorted(lista)
    mediana = lista_organizada[int(len(lista_organizada/2))]
    
def desvio_padrão(n, lista_medias, ):
    lista_medidas = lista_medias
    passo = 0
    for i in range(len(lista_medidas)):
        media_1 += lista[i]
    media = media_1 / (len(lista_medidas)+1)
    
    for i in range(len(lista_medidas)):
        lista_medidas[i] = lista_medidas[i]-media
        lista_medidas[i] = lista_medidas[i] ** 2
        passo += lista_medidas[i]
    
    passo2 = passo / (len(lista_medidas)-1)
    desvio = passo2 ** 1/2
    return desvio   


    
    
