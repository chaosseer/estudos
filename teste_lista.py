from lista_encadeada import *

def iniciar_teste(les,led):
    #lista encadeada simples
    les.inserir_inicio('a')
    les.inserir_inicio('b')
    les.inserir_fim('c')
    les.inserir_fim('d')
    les.inserir_fim('e')
    les.inserir_fim('f')
    les.inserir_fim('g')
    les.inserir_fim('h')
    #esperado: b a c d
    les.exibir()
    letras_simples.remover_valor('j')

    #lista encadeada dupla
    led.inserir_inicio('w')
    #led.exibir()
    print("---")
    led.inserir_fim('x')
    led.exibir()
    print("---")
    led.inserir_inicio('y')
    led.exibir()
    print("---")
    led.inserir_fim('z')
    led.exibir()
    print("---")
    #esperado y w x z 
    
def finalizar_teste(les,led):
    #lista encadeada simples
    les.exibir_primeiro()
    les.exibir_ultimo()
    print("lista toda")
    les.exibir()

    #lista encadeada dupla
    print("exibindo a dupla")
    led.exibir()
    print("exibindo a dupla agora ao contrario")
    led.exibir_reverso()

print("hora de testar essa bagaça")

letras_simples = lienc_simples()
letras_dupla = lienc_dupla()
iniciar_teste(letras_simples,letras_dupla)
finalizar_teste(letras_simples,letras_dupla)

letras_simples.remover_k(1)
#esperado: b a  d e  g h
letras_simples.exibir()
#letras_simples.remover_k(3)
letras_simples.exibir()