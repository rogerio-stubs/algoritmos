

def hanoi(disco, origem, destino, auxiliar):

    def mover(de, para):
        print('Mover da torre {} para a torre {}'
              .format(de, para))

    if disco >= 1:
        hanoi(disco-1, origem, auxiliar, destino)
        mover(origem, destino)
        hanoi(disco-1, auxiliar, destino, origem)