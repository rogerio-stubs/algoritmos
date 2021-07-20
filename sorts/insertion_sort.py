""" 
- pego um valor e verifico com o anterior, se o atual for menor altero as posições
- realizo esse procedimento até o valor anterior for menor que o atual

- É de simples implementação, leitura e manutenção.
- In-place: Apenas requer uma quantidade constante de O(1) espaço de memória adicional.
- Estável: Não muda a ordem relativa de elementos com valores iguais.
- Útil para pequenas entradas, muitas trocas, e menos comparações.
- Complexidade: O(n²).
"""

def insertion_sort(collection):
    size = len(collection)

    for j in range(1, size):
        key = collection[j]
        i = j - 1
        while i >= 0 and collection[i] > key:
            collection[i+1] = collection[i]
            i -= 1

        collection[i + 1] = key

    print(collection)
