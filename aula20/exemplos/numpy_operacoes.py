# =============================================================================
#  Enunciado
# =============================================================================

# A função numpy.linalg.solve() é usada para resolver sistemas de equações 
# lineares da forma Ax=B, onde:
#
#    A é uma matriz de coeficientes.
#    x é o vetor (ou matriz) de variáveis que queremos encontrar.
#    B é o vetor (ou matriz) de resultados.
#
# Essa função é muito mais eficiente do que o método da inversa da matriz 
# (np.linalg.inv(A) @ B), pois ela utiliza métodos de decomposição 
# (como a decomposição LU) que são numericamente mais estáveis e rápidos, 
# principalmente para matrizes grandes.

# =============================================================================
#  Header
# =============================================================================

import numpy as np

# =============================================================================
#  Main
# =============================================================================

# Matrizes de exemplo
print('A:')
A = np.array([
    [1, 2], 
    [3, 4]
])
print(A)

print('B:')
B = np.array([
    [21, 22], 
    [23, 24]
])
print(B)

# 1. Soma item por item
print('1. Soma')
A_mais_B = A + B
print(A_mais_B)

# 2. Subtração item por item
print('2. Subtracao')
B_menos_A = B - A
print(B_menos_A)

# 3. Multiplicação item por item ( matlab: A .* B )
print('3. Multiplicacao item por item')
A_vezes_B = A * B
print(A_vezes_B)

# 4. Multiplicação Matricial (Produto Escalar) ( matlab: A * B ) 
print('3. Multiplicacao de matriz')
A_multiplicado_B = A @ B
print(A_multiplicado_B)

