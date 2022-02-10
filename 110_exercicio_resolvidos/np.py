#importação de ferramentas
from numpy.lib.function_base import append
import numpy as np

list1 = input()
lista1 = list1.split()
vetor1 = np.asarray(lista1)
acu = 0
x = int(vetor1[0])
y = int(vetor1[1])
matriz =[]
print("X: ", x,"Y: ",y)
while acu < y:
  list2 = input()
  lista2 = list2.split()
  matriz.append(lista2)
  list2 = []
  lista2 = []
  vetor2 = []

  acu += 1

acu = 0 
notas = []
nota = 0
print(matriz)
while acu < x:
  for i in range(0,y,1):
    nota += float(matriz[i][acu])
    
  notas.append(nota)
  nota = 0
  acu += 1
print(notas)
for i in range(0,x-1):
  print(float(notas[i]/y))
