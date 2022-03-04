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
    
def armazena_nome(n): # = numero de alunos
    lista_nome = []
    acu = 1
    while acu <= n:
        lista_nome.append(str(input("Digite o nome do aluno de Ra de numero {}: ".format(acu))))
        acu += 1
    return lista_nome

def armazena_notas(n,lista):
    lita_notas = []
    acu = 0
    while acu < n:
        print("Insira a nota do aluno {} ".format(lista[acu]))
        n1 = float(input("Digite a primeira nota "))
        n2 = float(input("Digite a segunda nota "))        
        lista_notas.append([n1,n2])
    return lista_notas   
    
    
        
