#ENTRADA DA IMAGEM PRINCIPAL

tipo1 = str(input())
dimenssao1 = str(input())
matriz1 = []
matriz1t = []
di1=list(dimenssao1.split(" "))
cor1 = int(input())
n1 = int(di1[1])
m1 = int(di1[0])
a = 0

#criação da matriz 1

while a < n1:
    linha1 = str(input())
    matriz1 = linha1.split(" ")
    matriz1t.append((matriz1))
    a = a + 1

for i in range(n1):
    del(matriz1t[i][m1])
    print(matriz1t[i])


#ENTRADA DA IMAGEM SECWNDARIA

tipo2 = str(input())
dimenssao2 = str(input())
matriz2 = []
matriz2t = []
di2=list(dimenssao2.split(" "))
cor2 = int(input())
n2 = int(di2[1]) #n de linhas matriz 2
m2 = int(di2[0]) #n de col matriz 2
B = 0

#criação da matriz 1

while B < n2:
    linha2 = str(input())
    matriz2 = linha2.split(" ")
    matriz2t.append((matriz2))
    B = B + 1

for i in range(n2):
    del(matriz2t[i][m2])
    print(matriz2t[i])

print("x"*30)

type(matriz1t[0][0])
type(matriz2t[0][0])

m = []
c = 0
zeros = str
listax = []
matrizx = []


while c<n2:
    zeros = m2*"0"
    listax = list(zeros)
    matrizx.append(listax)
    c = c + 1

#for i in range(n2):

#    print(matrizx[i])


#print("x"*30)

matriz2tFH = matrizx
matriz2tFV = []
matriz2t90 = []
matriz2t180 = []


for i in range(0,n2,1):
    for j in range(m2,0,1):
        z = m2 + 1 - j
        matriz2tFH[i][z] = matriz2t[i][j]



print("x"*30)
for i in range(n2):
    print(matriz2tFH[i])

