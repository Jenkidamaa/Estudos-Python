#Dado um número inteiro n , e n inteiros separados por espaço como entrada, crie uma tupla,, daquelesinteiros. Em seguida, calcule e imprima o resultado de hash(t).

#Nota: hash() é uma das funções do __builtins__módulo, portanto não precisa ser importada.

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
    
