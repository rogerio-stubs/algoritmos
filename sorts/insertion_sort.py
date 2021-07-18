"""

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
