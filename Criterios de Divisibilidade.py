n = int(input())

# 1 : todo numero é divisivel por 1
# 2 : Divisibilidade por 2 o numero deve ser par

if n % 2 == 0: 
  print("Divisivel por 2")
# 3 : Divisibilidade por 3 a soma dos algarismo dos numeros deve ser divisivel por 3

n_lista = list(n)
for i in n_lista:
  soma += int(i)
if soma % 3 == 0:
  print("Divisivel por 3")
  
