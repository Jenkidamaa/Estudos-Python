def mutate_string(string, position, character):
    string = str(input())
    lista = list(string)
    position = int(input())
    character = str(input())
    lista[position] = character
    string = str(lista)
    
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
