if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maior = -999999
    for i in arr:
        if i > maior:
            maior = i
    a = 0
    while a < n:    
      for i in arr:             
        if maior == i:
          arr.remove(maior)
      a += 1
    maior = -9999999
      
    for i in arr:
        if i > maior:
            maior = i
      
    print(maior)
