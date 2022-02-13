#Printando formas geométricas
#quadrado
n = int(input())
contorno = str(input())
for i in range(n+1):
  if i == 0 or i == n:
    print(contorno*n)
  else:
    print(contador, (n-2)*" ",contador)
  
