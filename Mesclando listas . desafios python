##Inserir e intercalar duas listas do mesmo tamanho dadas pelo usuário

#lista1 = [1,3,5,7,9]
#lista2 = [2,4,6,8,10]
#lista3 = []

x = int(input("Insira o numero de elementos das listas: "))
lista1 = []
lista2 = []
lista3 = []

for i in range(x):
    lista1.append(int(input("Insira os elementos da primeira lista: ")))
    lista2.append(int(input("Insira os elementos da segunda lista: ")))



a = 0
b = 0
n = 0
while n < 5 :
    while a <= n:
        lista3.append(lista1[a])
        while b <= a:
            lista3.append(lista2[b])
            b = b + 1
        a = a + 1
    n = n + 1
    print("a",a,"b",b,"c",n)

print("Valores da primeira lista: ", lista1)
print("Valores da segunda lista: ", lista2)

print("Lista intercalada: ",lista3)
