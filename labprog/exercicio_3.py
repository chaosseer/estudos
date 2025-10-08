def exercicio_3(l1,l2):
    #retorna uma lista com valores alternados de outras duas
    l3=[]
    i=0
    while len(l3) < len(l1)+len(l2):
        try: l3.append(l1[i]) 
        except: 
            IndexError
        try: l3.append(l2[i])
        except: 
            IndexError
        i+=1
    print(l3)
    return l3