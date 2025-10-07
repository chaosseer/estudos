class No:
    def __init__(self,valor, a, p):
        self.info = valor
        self.ant = a
        self.prox = p

class LDDE:
    def __init__(self):
        self.tamanho = 0
        self.prim = None

    def estaVazia(self):
        return self.tamanho == 0
    
    def inserePrim(self,valor):
            if self.estaVazia():
                print(f"Inserindo {valor}")
                self.prim = No(valor,None,None)
                self.prim.ant = self.prim.prox = self.prim
                self.tamanho += 1
            else:
                print("Erro: primeiro elemento já inserido")
    
    def buscar(self,valor):
        if not self.estaVazia():
            if self.prim.info == valor:
                print(f"Elemento {valor} consta na lista")
                return True
            elif self.tamanho > 1:
                aux = self.prim
                while aux.prox != self.prim:
                    if aux.prox.info == valor:
                        print(f"Busca encerrada - elemento {valor} consta na lista")
                        return True
                    else:
                        aux = aux.prox
                print(f"Busca encerrada - elemento {valor} não consta na lista")
                return False
            else:
                print(f"Elemento {valor} não consta na lista")
                return False
        else:
            print("Erro - lista vazia;")
            return False
        

    def inserirAntesDe(self,valor1,valor2):
            if self.buscar(valor1):
                print(f"\nErro: valor {valor1} já consta na lista;")
            elif not self.buscar(valor2):
                print("\nErro: valor posterior informado não encontrado;")
            else:
                aux = self.prim
                if aux.info == valor2:
                    self.prim.ant = self.prim.prox = No(valor1,self.prim,self.prim)
                    print("Inserção concluída")
                else:
                    while aux.info != valor2 and aux.prox != self.prim:
                        aux = aux.prox
                    aux.ant.prox = aux.ant = No(valor1,aux.ant,aux)
                    self.tamanho += 1
                    print("Inserção concluída")
            print("Fim do método inserirAntesDe()")
    
    def exibirLista(self):
        print("Exibindo elementos da lista a partir do primeiro...")
        if not self.estaVazia():
            print(f"{self.prim.info},")
            aux = self.prim
            while aux.prox != self.prim:
                aux = aux.prox
                print(f"{aux.info},")
            print("Todos os elementos foram listados")
        else:
            print("Lista vazia, nada pra ver aqui...")
            