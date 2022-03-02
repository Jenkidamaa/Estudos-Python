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

# 4 : Divisibilidade por 4 se os dois últimos algarismos forem divisíveis por 4, (ou se terminar em 00) então o número também é divisível por 4.

n_div_4 = n_lista[len(n_lista-2)] + n_lista[len(n_lista-1)]
if int(n_div_4) % 4 == 0:
  print("Divisivel por 4")
  
# 5 : Divisibilidade por 5 se um número tiver como ultimo algarismo das unidades 0 ou 5 então é divisível por 5.

if n_lista[len(n_lista-1)] == 0 or n_lista[len(n_lista-1)] == 5:
  print("Divisivel por 5")
  
  
  
