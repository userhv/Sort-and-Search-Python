import random

class Ordenador:
    def selectSort(self,lista):
        
        fim = len(lista)

        for i in range(fim-1): #inicialmente o menor elemento ja visto é o i-ésimo numero
            posicaoDoMinimo = i        
            for j in range(i+1,fim):
                if lista[j] < lista[posicaoDoMinimo]:   #coloca o menor elemento encontra no inicio da sub-lista
                    posicaoDoMinimo = j                #para isso troca de lugar os elementos da posição i e posicaoDoMinimo
            
            lista[i] , lista[posicaoDoMinimo] = lista[posicaoDoMinimo] , lista[i]
        return lista

    def bubbleSort(self,lista):
        
        fim = len(lista)

        for i in range(fim-1,0,-1):
            troca = False #serve pra que caso ele não faça troca de nada quando tiver passando pelo i ele encerra
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1] , lista[j]
                    troca = True
            if not troca:
                return lista
    
    def insertionSort(self,lista):
    
        for i in range(len(lista)):            
            for j in range(i,0,-1):
                if lista[j] < lista[j-1]:
                    lista[j], lista[j-1] = lista[j-1], lista[j]
        return lista
    
    def mergeSort(self,lista):
        if len(lista) <= 1:
            return lista
        
        meio = len(lista) // 2

        ladoEsquerdo = self.mergeSort(lista[:meio])
        ladoDireito = self.mergeSort(lista[:meio])

        return self.merge(ladoEsquerdo,ladoDireito)

    def merge(self,ladoEsquerdo,ladoDireito):
        if not ladoEsquerdo:
            return ladoDireito
        
        if not ladoDireito:
            return ladoEsquerdo
        
        if ladoEsquerdo[0] < ladoDireito[0]:
            return [ladoEsquerdo[0]] + self.merge(ladoEsquerdo[1:], ladoDireito)

        return [ladoDireito[0]] + self.merge(ladoEsquerdo, ladoDireito[1:])



def main():    
    lista = [random.randrange(100) for x in range(6)]
    o = Ordenador()
    o.selectSort(lista)
    print(lista)

main()