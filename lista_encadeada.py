#Lista Encadeada

class No:#pra encadamento simples
    def __init__(self, info, proximo):
        self.info = info
        self.prox = proximo

class No_duplo(No):#pra encadeamento duplo
    def __init__(self,anterior,info,proximo):
        super().__init__(info,proximo)
        self.ant = anterior

class lienc_simples:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    #inserções
    def inserir_inicio(self,info):
        if self.quant == 0:
            self.prim=self.ult = No(info,None)
        else:
            self.prim = No(info,self.prim)#o primeiro agora é o segundo
        self.quant += 1
        

    def inserir_fim(self,info):
        if self.quant == 0:
            self.prim = self.ult = No(info,None)
        else:
            self.ult.prox = self.ult = No(info, None)#o ultimo agora é o antepenultimo
        self.quant += 1
        
    
    #remoções
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -=1
        
    
    def remover_fim(self):
        if self.quant==1:
            self.prim = self.ult = None
        else:
            n = self.prim
            while n.prox!= self.ult:
                n = n.prox
            n.prox = None
            self.ult = n
        self.quant -= 1
        
    def remover_valor(self,valor):
        if self.prim.info == valor:
                self.remover_inicio()
        elif self.ult.info == valor:
                self.remover_fim()
        else:
            aux = self.prim
            while aux.prox.info != valor:
                aux = aux.prox
            if aux.prox.info == valor:
                aux.prox = aux.prox.prox
                self.quant -= 1
            else: print("Valor não encontrado")    

    #exibições (caso necessario, transformar os prints em retornos pra serem usados no print do módulo)
    def exibir(self):
        n = self.prim
        while n != None:
            print(n.info,"\n")
            n = n.prox        
    def exibir_primeiro(self):
        print("Primeiro elemento:",self.prim.info)   
    def exibir_ultimo(self):
        print("Último elemento:",self.ult.info)

    #buscas
    def buscar_valor(self,i):#retorna o No que possui o valor i, ou None caso não o encontre
        n = self.prim
        while n != None:
            if n.info == i:
                return n
            n = n.prox
        return n
    def remover_k(self,k):
        i = 1
        n = self.prim
        t = self.quant
        k_esimos=[]
        while i <= t:
            if i%k == 0: #se i for multiplo de k
                k_esimos.append(n)
            n = n.prox    
            i += 1
        for item in k_esimos:
            if item == self.prim:
                self.remover_inicio()
            elif item == self.ult:
                self.remover_fim()
            else:
                aux = self.prim
                while aux.prox != item:
                    aux = aux.prox
                aux.prox = aux.prox.prox
                self.quant -= 1
    
    #outras
    def tamanho(self):#retorna em int o tamanho atual da lista
        return self.quant
    def vazia(self):#retorna True or False caso a lista tenha ou não algum elemento
        return self.quant == 0 

class liencs_circular(lienc_simples):
    def inserir_inicio(info,self):
        super().inserir_inicio(info,self)
        self.ult.prox = self.prim

    def inserir_fim(info,self):
        self.ult.prox = No(info,self.prim)

class lienc_dupla(lienc_simples):
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    #inserções
    def inserir_inicio(self,info):
        if self.quant == 0:
            self.prim = self.ult = No_duplo(None,info,None)
        else:
            self.prim.ant = self.prim = No_duplo(None,info,self.prim)
        self.quant += 1

    def inserir_fim(self,info):
        if self.quant == 0:
            self.prim = self.ult = No_duplo(None,info,None)
        else:
            self.ult.prox = self.ult = No_duplo(self.ult,info,None)
        self.quant += 1
    
    #remoções
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -=1

    def remover_fim(self):
        if self.quant==1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant 
            self.ult.prox = None
        self.quant -= 1

    def remover_No(self,n):
        if self.quant==1:
            self.prim = self.ult = None
        else:
            n.ant.prox = n.prox
            n.prox.ant = n.ant
            self.quant -= 1

    #exibições
    def exibir(self):
        n = self.prim
        while n != None:
            print(n.info,"\n")
            n = n.prox
    def exibir_reverso(self):
        n=self.ult
        while n != None:
            print(n.info,"\n")
            n = n.ant
    def exibir_primeiro(self):
        print("Primeiro elemento:",self.prim.info)   
    def exibir_ultimo(self):
        print("Último elemento:",self.ult.info)
    
    def remover_meio(self):
        i = 1
        aux = self.prim
        while i< self.quant/2:
            aux = aux.prox
        self.remover_No(aux) 

    

    def buscar_valor(self,i):#retorna o No que possui o valor i, ou None caso não o encontre
        n = self.prim
        while n != None:
            if n.info == i:
                return n
            n = n.prox
        return n
  
    def anterior_de(self,i):#retorna o Nó que vem antes o que guarda o valor i
        return self.buscar_valor(self,i).ant
    def posterior_de(self,i):#retorna o Nó que vem após o que guarda o valor i
        return self.buscar_valor(self,i).prox
    def possui_irmaos(self,i):#retorna se o Nó com valor i possui elementos antes e depois dela
        return (self.anterior_de(self,i)!=None and self.posterior_de(self,i)!=None)
        
        
        



