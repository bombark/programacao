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

# Problema de Exemplo:
#    x + 2y = 5
#   3x + 4y = 11

# Definir a matriz de coeficientes A
A = np.array([[1, 2], [3, 4]])
B = np.array([5, 11])

# Resolver o sistema de equações
x = np.linalg.solve(A, B)

# Exibir a solução
print(f"O vetor de soluções (x, y) é: {x}")

