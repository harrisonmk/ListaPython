from No import No


class Lista:

    def __init__(self):
        self.primeiroNo = None
        self.ultimoNo = None



    def isEmpty(self):
        return self.primeiroNo is None

    def tamanho(self):
        atual = self.primeiroNo
        cont = 0
        while atual is not None:
            cont = cont + 1
            atual = atual.getProx()
        return cont

    def insereNoComeco(self, valor):
        novoNo = No(valor)
        if self.isEmpty():
            self.primeiroNo = self.ultimoNo = novoNo
        else:
            novoNo.setProx(self.primeiroNo)
            self.primeiroNo = novoNo

    def insereNoFinal(self, valor):
        novoNo = No(valor)
        if self.isEmpty():
            self.primeiroNo = self.ultimoNo = novoNo
        else:
            self.ultimoNo.setProx(novoNo)
            self.ultimoNo = novoNo

    def removeComeco(self):

        if self.isEmpty():
            print("Impossivel Remover Lista Vazia")
        primeiroValorNo = self.primeiroNo.getElemento()
        if self.primeiroNo == self.ultimoNo:
            self.primeiroNo = self.ultimoNo = None
        else:
            self.primeiroNo = self.primeiroNo.getProx()
            return primeiroValorNo

    def removeFinal(self):

        if self.isEmpty():
            print("Impossivel Remover Lista Vazia")
        ultimoValorNo = self.ultimoNo.getElemento()
        if self.primeiroNo is self.ultimoNo:
            self.primeiroNo = self.ultimoNo = None
        else:
            noAtual = self.primeiroNo
            while noAtual.getProx() != self.ultimoNo:
                noAtual = noAtual.getProx()
            noAtual.setProx(None)
            self.ultimoNo = noAtual
        return ultimoValorNo

    def busca(self, valor):
        if self.isEmpty == True:
            return None
        i = self.primeiroNo
        while i != None:
            if i.getElemento() == valor:
                return i
            i = i.getProx()
        return None

    def listar(self):

        if self.primeiroNo == None:

            print("Lista Vazia")
        else:

            temp = self.primeiroNo
        while temp != None:
            print("Valor: ", temp.getElemento())
            temp = temp.getProx()

    def __str__(self):
        if self.isEmpty():
            return "Lista Vazia"
        noAtual = self.primeiroNo
        palavra = "a lista eh: "
        while noAtual is not None:
            palavra += str(noAtual.getElemento()) + " "
            noAtual = noAtual.getProx()
        return palavra

    def bubleSortPython(self, arraytoSort):
        swapFlag = True
        while swapFlag:
            swapFlag = False
            for i in range(len(arraytoSort) - 1):
                if arraytoSort[i] > arraytoSort[i + 1]:
                    arraytoSort[i], arraytoSort[i + 1] = arraytoSort[i + 1], arraytoSort[i]

                    print("Swapped: {} with {}".format(arraytoSort[i], arraytoSort[i + 1]))
                    swapFlag = True
        return arraytoSort

    def insertion_sort(self, list):

        for index in range(1, len(list)):
            value = list[index]
            i = index - 1
            while i >= 0:
                if value < list[i]:
                    list[i + 1] = list[i]
                    list[i] = value
                    i = i - 1
                else:
                    break;


    def mergeSorte(self, a, b):
        resultado = None;

        if (a == None):
            return b

        if (b == None):
            return a;

        if (a.elemento <= b.elemento):
            resultado = a
            resultado.Prox = mergeSorte(a.Prox, b)
        else:
            resultado = b;
            resultado.Prox = mergeSorte(a, b.Prox)

        return resultado

    def mergeSort(self, h):

        if (h == None or h.prox == None):
            return h

        meio = getMiddle(h)
        proxDoMeio = meio.getProx()

        meio.Prox = None

        esquerda = mergeSort(h)

        direita = mergeSort(proxDoMeio)

        sortedlist = mergeSorte(esquerda, direita)
        return sortedlist

    def getMiddle(self, h):

        if (h == None):
            return h

        parteRapida = h.getProx()
        parteLenta = h

        while (parteRapida != None):
            parteRapida = parteRapida.getProx();
            if (parteRapida != None):
                parteLenta = parteLenta.getProx();
                parteRapida = parteRapida.getProx();

        return parteLenta;
    
    
    
    def sort1(self,array):
        for p in range(0, len(array)):
            current_element = array[p]

            while p > 0 and array[p - 1] > current_element:
                array[p] = array[p - 1]
                p -= 1

            array[p] = current_element