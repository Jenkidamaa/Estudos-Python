if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maior = 0
    for i in arr:
        if i > maior:
            maior = i
    for i in range(len(arr)):
        if i == maior:
            indice = arr.index(i)
            del arr[indice]
    maior = 0
    for i in arr:
        if i > maior:
            maior = i
        
    print(maior)
