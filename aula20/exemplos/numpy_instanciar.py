
import numpy as np


# 1a. Cria uma matriz a partir de uma Matriz Nativa
print('1a:')
matriz = np.array([ [1, 2, 3],
                    [4, 5, 6]])
print(matriz)


# 1b. Cria uma matriz a partir de uma Matriz Nativa
print('1b:')
nativa = [ [1, 2, 3], [4, 5, 6] ]
matriz = np.array(nativa)
print(matriz)


# 2. Cria uma matriz 3x4 preenchida com 0
print('2:')
matriz = np.zeros((3, 4))
print(matriz)


# 3. Cria uma matriz 2x2 preenchida com 1
print('3:')
matriz = np.ones((2, 2))
print(matriz)


# 4. Cria uma matriz identidade de 3x3
print('4:')
matriz_identidade = np.eye(5)
print(matriz_identidade)


# Cria uma matriz 2x3 com números aleatórios entre 0 e 1
print('5:')
matriz_aleatoria = np.random.rand(2, 3)
print(matriz_aleatoria)