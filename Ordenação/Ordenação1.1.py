l = [8,7,6,5,4,3,2,1] # [2,2,4,5,7,8,8,45]
maior = 0
menor = 9999999999
inicio = 0
fim = len(l)-1
PI = bool
i_fim = 0
i_inicio = 0
a_inicio = 0
a_fim = 0

if len(l)%2 == 0:
  PI = True
else:
  PI = False
acu = 0
rotina = int(len(l)/2)
print(rotina)
if PI == True:
  while acu<int(rotina):
    for i in range(inicio,fim,1):
      if maior < l[i] :
        maior = l[i]
        a_fim = l[fim]
        i_fim = i
      if menor > l[i]:
        menor = l[i]
        a_inicio = l[inicio]
        i_inicio = i
    l[inicio] = menor
    l[fim] = maior
    l[i_inicio] = a_inicio
    l[i_fim] = a_fim
    maior = 0
    menor = 9999999999
    inicio += 1
    fim -= 1
    acu += 1
    i_inicio = 0
    print(l)
