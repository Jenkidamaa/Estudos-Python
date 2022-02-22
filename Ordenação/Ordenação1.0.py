l = [8,2,45,2,4,5,7,8]
maior = 0
menor = 9999999999
inicio = 0
fim = len(l)-1
PI = bool

if len(l)%2 == 0:
  PI = True
else:
  PI = False
acu = 0
rotina = int(len(l)/2)

if PI == True:
  while acu<int(rotina):
    for i in range(inicio,fim,1):

    
      for i in l:
        if maior < i :
          maior = i
        if menor > i:
          menor = i
      l[inicio] = menor
      l[fim] = maior
      maior = 0
      menor = 9999999999
      inicio += 1
      fim -= 1
      acu += 1
print(l)
##Com a primeira tentativa de criação do código acontece a substituição dos valores das posições "inicio" e "fim" perdendo-os ao decorrer do código, 
##uma alternativa para contornar a situação seria armazenar esses valores e substitui-los nas posições de são retirados "maiores" e "menores".
