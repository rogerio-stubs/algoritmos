"""
- Pegar o elemento atual comparar com o proximo.
- Se o próximo for menor que o atual eles trocam de posição.
- repetir esse processo até o vetor ficar totalmente ordenado.

- Complexidade: O(n²).
- Não é recomendado para programas que precisem de velocidade e 
    operem com quantidade elevada de dados.
"""

def bubble_sort(collection):
    elementos = len(collection)-1
    ordenado = False

    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if collection[i] > collection[i+1]:
                collection[i], collection[i+1] = collection[i+1], collection[i]
                ordenado = False

if __name__ == '__main__':
    collection = [7, -1, 4, -7, 2, 3, -9, 5, 1, 8]
    bubble_sort(collection)
    print(collection)