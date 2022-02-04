#entrada de uma string em linha
eq = input()
#remoção dos espaços, colocando cada termo e operador dentro de uma lista 
p = eq.split()
#for para concatenar e variavel "a" para o indice da lista
a = 0
for i in p:
  s += i
  
for i in s:
  if i == "x":
    s[a] = 2
  a += 1
  
  
