#programa ordenação das panquecas de acordo com o o diametro

#Entrada

#adiciona e transforma o inteiro em uma lista de strings
valores = list(input())
#transforma strings em inteiro
panquecas = []
for val in valores:
    panquecas.append(int(val))


armazena = int
#a = variavel booleana para determinar o fim do processo

indice = int
a = False
i = len(panquecas)-1
acu = 0
for j in range(1, len(panquecas), 1):
   if panquecas[j - 1] < panquecas[j]:

      acu = acu + 1
   if acu == len(panquecas):
      a = True


while a == False:
   acu = 0
   for j in range(1, len(panquecas), 1):
      if panquecas[j-1] < panquecas[j]:
         acu = acu + 1
      if acu == len(panquecas):
         a = True
   armazena = max(panquecas[0:i])
   indice = panquecas.index(armazena)
   panquecas.__delitem__(indice) #elimina o item da lista pois ja esta armazenado na variavel armazena

   #Caso em que o numero a ser alocado na posição correta da lista esta na primeira posição


   if indice == 0:
      print("Posicionando a panqueca ", armazena)
      panquecas.insert(i, armazena)
      del panquecas[0]
      i = i - 1
   else:
      print("Posicionando a panqueca ", armazena)
      panquecas.insert(0 , armazena)
      print("Primeira inversao: ", panquecas)
      b = panquecas.pop(0)
      panquecas.insert(i , b)
      print("Segunda inversao: ", panquecas)
      i = i - 1


if a == True:
   print(panquecas)

