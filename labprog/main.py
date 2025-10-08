from exercicio_1 import *
from exercicio_2 import *
from exercicio_3 import *
from exercicio_4 import *
ex=-1
li=['asdas','sad','fd','asdasdasd','s','dasd']
st=['1','2','3','4','5']
while ex != 0:
    ex = int(input(
    "Seja bem-vindo ao programa main.py. Por favor, escolha a opção desejada:\n"
    "1 – Exercício 1\n"
    "2 – Exercício 2\n"
    "3 – Exercício 3\n"
    "4 – Exercício 4\n"
    "5 – Exercício 5\n"
    "6 – Exercício 6\n"
    "7 – Exercício 7\n"
    "8 – Exercício 8\n"
    "9 – Exercício 9\n"
    "10 – Exercício 10\n"
    "0 – Sair\n"))
    if ex == 0:
        break
    if ex > 0 or ex < 9:
        print("abrir_exercicio",ex)
        if ex == 1:
            exercicio_1(li)
        elif ex == 2:
            exercicio_2(li)
        elif ex == 3:
            exercicio_3(li,st)
        elif ex == 4:
            exercicio_4(st)
        elif ex == 5:
            exercicio_5()
        elif ex == 6:
            exercicio_6()
        elif ex == 7:
            exercicio_7()
        elif ex == 8:
            exercicio_8()