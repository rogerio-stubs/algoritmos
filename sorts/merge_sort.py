"""
- Divida o vetor em duas metades. merge_sort()
- Ordene recursivamente cada metade. merge()
- Mescle as duas metades do vetor, isto é, combine as duas metades para formar um único arranjo.

- Complexidade: Pior caso O(nlog(n))
- Não é in-place pois utilizamos um vetor auxiliar (sup)
"""

def merge(collection, sup, left, half, right):
    for k in range(left, right + 1):
        sup[k] = collection[k]
    
    i = left
    j = half + 1

    for k in range(left, right + 1):
        if i > half:
            collection[k] = sup[j]
            j += 1
        elif j > right:
            collection[k] = sup[i]
            i += 1
        elif sup[j] < sup[i]:
            collection[k] = sup[j]
            j += 1
        else:
            collection[k] = sup[k]
            i += 1

def merge_sort(collection, sup, left, right):
    if right <= left:
        return

    half = (left + right) // 2

    merge_sort(collection, sup, left, half)

    merge_sort(collection, sup, half + 1, right)

    merge(collection, sup, left, half, right)


if __name__ == '__main__':
    collection = [7, -1, 4, -7, 2, 3, -9, 5, 1, 8]
    size = len(collection)
    aux = [0] * size
    merge_sort(collection, aux, 0, size - 1)
    print(collection)