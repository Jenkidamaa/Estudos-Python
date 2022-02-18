n = int(input())
arr = map(int, input().split())



maior = 0
for i in arr:
    if i > maior:
        maior = i
for i in range(len(arr)):
    if i == maior:
        arr.del(i)
maior = 0
for i in arr:
    if i > maior:
        maior = i
        
print(maior)
