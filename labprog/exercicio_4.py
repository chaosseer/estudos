def exercicio_4(lista):
    pares=[]
    for i in range(len(lista)):
        if i%2 ==0:
            pares.append(lista[i])
    return pares