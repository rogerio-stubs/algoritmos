from lista_encadeada import *

if __name__ == '__main__':
    lista = ListaEncadeada()
    lista.inserir_no_inicio(5)
    print(lista)

    lista.inserir_depois(lista.cabeca, 4)
    print(lista)

    lista.inserir_depois(lista.cabeca, 3)
    print(lista)
