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
  
# 6 : Divisibilidade por 6 se um número for divisível por 2 e por 3.


# 7 : Divisibilidade por 7, separar o número do seu último algarismo. Se o 1° grupo de algarismos separados menos o dobro do último 
#algarismo for múltiplo de 7, então o número original é divisível por 7.

n_div_7 = int(n_lista[len(n_lista-1)]
for i in range(0,len(n_lista-2)):
  n_div_7_primeiros += n_lista[i]
n_div_7_primeiros_int = int(n_div_7_primeiros)
if (n_div_7_primeiros_int - 2 * n_div_7) % 7 == 0:
  print("Divisivel por 7")
              
              

# 8 : Divisibilidade por 8 se os três últimos algarismos forem divisíveis por 8, (ou se terminar em 000) então o número também é divisível por 8
