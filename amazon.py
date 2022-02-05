class Solution:
    def majorityElement(self, A):
        vezes = 0
        a = len(A)
        acu = 0
        x = 0; lista = []; n = 0
        while acu < a:
            for i in A:
                if i == A[vezes]:
                    x =+ 1
                vezes += 1
            lista.append(x)
            vezes = 0
            acu += 1
            x = 0
        maior = 99999999
        for i in range(len(lista)):
            if i < lista[i]:
                maior = lista[i]
        soma = 0
        for i in lista:
            soma += i
        return print("{} which occurs {} times which is greater than {}/2.", format(n , soma))
        

