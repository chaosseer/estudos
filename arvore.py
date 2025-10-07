class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def busca(self, valor):
        if valor == self.info:
            return True

        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
            
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)
            
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total
    
    def qualOrdem(self):
        if self.dir != None:
            self.dir.qualOrdem()
        print(self.info,end=" ")
        if self.esq != None:
            self.esq.qualOrdem()

class Tree:
    def __init__(self):
        self.raiz = None
    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.qualOrdem()



