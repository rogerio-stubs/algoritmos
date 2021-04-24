class NodeLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
    
    def __repr__(self):
        return '[' + str(self.cabeca) + ']'

    def inserir_no_inicio(self, novo_dado):
        novo_nodo = NodeLista(novo_dado)

        novo_nodo.proximo = self.cabeca

        self.cabeca = novo_nodo

    def inserir_depois(self, nodo_anterior, novo_dado):
        assert nodo_anterior

        novo_nodo = NodeLista(novo_dado)

        novo_nodo.proximo = nodo_anterior.proximo

        nodo_anterior.proximo = novo_nodo

    def busca(self, valor):
        corrente = self.cabeca
        if corrente is None:
            return 'Lista vazia!'

        while corrente.dado != valor:
            if corrente.proximo is None:
                return False
            corrente = corrente.proximo
        return True

    def remove(self, valor):
        assert self.cabeca

        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            anterior = None
            corrente = self.cabeca
            while corrente and corrente.dado != valor:
                anterior = corrente
                corrente = corrente.proximo

            if corrente:
                anterior.proximo = corrente.proximo
            else:
                anterior.proximo = None