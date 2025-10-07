from LDDE import *

lista = LDDE()
print("Ok, vamos ver se isso aqui funciona...")
opt = int(input(
"""1 -  usar a inserePrim();
    \n2 - usar a insereAntesDe();
    \n3- exibir os elementos da lista(usando exibirLista());
    \n0 - Sair
    \nSua escolha? """))
while opt != 0:
    if opt == 1:
        v = input("Qual valor a gente põe no primeiro então? ")
        lista.inserePrim(v)

    elif opt == 2:
        if lista.estaVazia():
            print("\nErro: lista vazia;")
        else:
            v1 = input("Qual valor a gente põe antes do próximo? ")
            v2 = input("E antes de qual? ")
            lista.inserirAntesDe(v1,v2)
            
    elif opt == 3:
        lista.exibirLista()

    print("\nOk, vamo de novo\n")
    opt = int(input(
    """1 -  usar a inserePrim();
    \n2 - usar a insereAntesDe()
    \n0 - Sair
    \nSua escolha? """))
