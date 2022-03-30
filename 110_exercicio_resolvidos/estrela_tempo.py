import time
#laço 1
countTimer1 = 0
sleepTime1 = 1
#laco 2
countTimer2 = 0
sleepTime2 = 1
#laco 3
countTimer3 = 0
sleepTime3 = 1
#laço 4
countTimer4 = 0
sleepTime4 = 1
#laco 5
countTimer5 = 0
sleepTime5 = 1
#parte superior triangulo
#espacos
a1= 10
#input da forma a ser prechida em seguida o prenchimento da estrela 

forma = str(input("Insira a forma : "))
a2 = 1

#numero de interacoes do laco
a=0
#laco 1
while a < 11:
  time.sleep(sleepTime1)
  countTimer1 += sleepTime1
  print(14*" "+a1*" "+a2*forma+a2*forma)
  a1 -=1
  a2 += 1
  a+=1
#	
a3 = 50

a4 = 0
#parte supeior do meio
#laco 2
while a4 <8:
  time.sleep(sleepTime2)
  countTimer2 += sleepTime2
  print(" "*a4+forma*a3)
  a4+=1
  a3 -= 2
#laco 3	
while a4 <8:
  time.sleep(sleepTime3)
  countTimer3 += sleepTime3
  print(" "*a4+forma*a3)
  a4+=1
  a3 -= 2
#parte inferior do meio
#laco 4

a5 = 8
a6 = 36	
while a5 > 0:
  time.sleep(sleepTime4)
  countTimer4 += sleepTime4
  print(" "*a5+forma*a6)
  a5-=1
  a6 += 2
	
#parte inferior da cauda
#laco 5

while a >= 0:
  time.sleep(sleepTime5)
  countTimer5 += sleepTime5
  print(14*" "+a1*" "+a2*forma+a2*forma)
  a -= 1
  a1 += 1
  a2 -= 1
