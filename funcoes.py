import numpy as np
def para_one_hot(palavra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    matriz = np.zeros((len(alfabeto), len(palavra)))
    palavra = palavra.lower()
    for i in range(len(palavra)):
        letra = palavra[i]
        indice = alfabeto.index(letra)
        matriz[indice][i] = 1
    return matriz
# print(para_one_hot('bananazz'))


