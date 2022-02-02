n = int(input()); l = str(input()); b = 0
lista = list(str(n))

if 0 < n < 10:
  b += 1
if 10 <= n < 100:
  if lista [0] == lista[1]:
    b += 1

lista2 = []

for i in range(0,len(l)):
  print(l[i]+l[i+1])
