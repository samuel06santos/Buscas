import numpy as np
import timeit

def busca_linear(lista, key):
    lista = sorted(lista)
    len_lista = len(lista)

    count = 0
    for i in range(len_lista):
        count += 1
        if lista[i] == key:
            return i, count
    return -1


def busca_binaria(lista, key):
    lista = sorted(lista)
    len_lista = len(lista)
    first, last = 0, len_lista - 1

    count = 0
    while first <= last:
        count += 1
        middle = (first + last) // 2
        
        if lista[middle] == key:
            return middle, count
        
        elif lista[middle] < key:
            first = middle  + 1
        
        elif lista[middle] > key:
            last  = middle - 1
    return -1


def main():
    
    lista = np.arange(1, 1024+1)

    key = 1024

    pos_l, ite_l = busca_linear(lista, key)
    pos_b, ite_b = busca_binaria(lista, key)

    print(f'{key} está na posição: {pos_b} ([{lista[0]}, {lista[-1]}]), {ite_b} iterações.')
    print(f'{key} está na posição: {pos_l} ([{lista[0]}, {lista[-1]}]), {ite_l} iterações.')
    

if __name__ == "__main__":
    main()