"""
- Percorre o vetor, buscando a menor posição.
- Percorre o vetor, buscando o menor elemento.
- Altere a posição dos elementos.

- Não precisa de um vetor auxíliar (in-place), por isso ocupa menos memória
- Veloz para vetores de tamanho pequeno, mas lento para vetores grandes
- Ele não estável
- Complexidade: O(n^2)
"""

def selection_sort(collection):
    size = len(collection)

    for i in range(size):
        minimum = i
        for x in range(i+1, size):
            if collection[minimum] > collection[x]:
                minimum = x
            
        collection[i], collection[minimum] = collection[minimum], collection[i]

    print(collection)