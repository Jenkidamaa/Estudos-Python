if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maior = 0
    for i in arr:
        if i > maior:
            maior = i
    print(arr)
    for i in arr:
        print(i)
        if i == maior:
          arr.remove(maior)
    maior = 0
    for i in arr:
        if i > maior:
            maior = i
    print(arr)    
    print(maior)
