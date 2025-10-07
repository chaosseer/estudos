class No:
    def __init__(self,valor):
        self.info = valor
        self.dir = self.esq = None

    def inserir(self,valor):
        if valor <= self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.inserir(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.inserir(valor)

    def busca(self,valor):
        if self.info == valor:
            return True
        elif valor > self.info:
            self.dir.busca(valor)
        else:
            self.esq.busca(valor)
        
    def imprimeDescDireita(self,valor):
        print(self.info)
        if self.info == valor:
            return
        else:
            if self.dir != None and self.info < valor:
                self.dir.imprimeDescDireita(valor)
            else:
                if self.esq != None and self.esq.info > valor:
                    self.esq.imprimeDescDireita(valor)


        
            

class Tree:
    def __init__():
        raiz = None
    def inserir():
        if raiz != None:
            raiz = No()