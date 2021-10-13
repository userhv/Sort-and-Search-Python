import random

class Buscador:
    def buscaSequencial(self,lista,x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return False #mensagem de não encontrado

    def buscaBinaria(self,lista,x):
        primeiro = 0
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro+ultimo)//2
            if lista[meio] == x:
                return meio
            else: #parte a lista na metade e descarta um pedaço dependendo do valor meio
                if x < lista[meio]: 
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return False




def main():
    listaTeste = [random.randrange(10)for x in range(6)]
    o = Buscador()
    o.buscaBinaria(listaTeste,4)
    print(listaTeste)

main()