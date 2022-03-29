
#parte superior triangulo
#espacos
a1= 10
#input da forma a ser prechida em seguida o prenchimento da estrela 

forma = str(input("Insira a forma : "))
a2 = 1

#numero de interacoes do laco
a=0

while a < 11:
	print(14*" "+a1*" "+a2*forma+a2*forma)
	a1 -=1
	a2 += 1
	a+=1
#	
a3 = 50

a4 = 0
#parte supeior do meio
while a4 <8:
	print(" "*a4+forma*a3)
	a4+=1
	a3 -= 2
	
while a4 <8:
	print(" "*a4+forma*a3)
	a4+=1
	a3 -= 2
#parte inferior do meio
a5 = 8
a6 = 36	
while a5 > 0:
	print(" "*a5+forma*a6)
	a5-=1
	a6 += 2
	
#parte inferior da cauda

while a >= 0:
	print(14*" "+a1*" "+a2*forma+a2*forma)
	a -= 1
	a1 += 1
	a2 -= 1
