n = int(input())

gabarito_aluno = list(input())
gabarito_oficial = list(input())
acu = 0
for i in range(n):
  if gabarito_aluno[i] == gabarito_oficial[i]:
    acu += 1
print(acu)
