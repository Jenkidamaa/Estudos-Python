n = int(input())
arr = map(int, input().split())

for i in arr:
    print(i)
sort(arr)
print()
for i in arr:
    print(i)

maior = 0
for i in arr:
    if i > maior:
        maior = i
print(maior)
