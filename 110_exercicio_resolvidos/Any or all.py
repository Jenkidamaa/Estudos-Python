# Enter your code here. Read input from STDIN. Print output to STDOUT
palindromo = int(input())
var = 0
if 1 < palindromo <=10:
  var += 1
if 10 < palindromo < 100:
  cs = str(palindromo)
  if cs[0] == cs [1]:
    var += 1

a = input()
b = ""
c = 0
d= []
f = 0
while c<palindromo:
  if f < len(a):
    while a[f] != " " and f < len(a):
      b += a[f]
      f += 1
      if f == len(a):
          break

  f += 1
  d.append(b)
  b = ""
  c += 1 

lista = []
for i in d:
  lista.append(int(i))
i = len(lista)-1

cont = 0
while lista[i] >= 0 :
    #print(lista[i])
    if i == 0:
      break
    i -= 1
    if i == 0:
      break


if i == 0:
  var += 1
if var == 2:
  print(True)
else:
  print(False)
