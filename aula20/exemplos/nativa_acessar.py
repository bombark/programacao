# Exemplos de Iteração sobre uma Matriz Nativa

# Matriz de exemplo
matriz = [
    #  0   1   2 - (coluna)
    [ 16, 32, 64],    # linha 0 
    [ 17, 33, 65],    # linha 1
    [ 18, 34, 66]     # linha 2
]


# =============================================================================
#  1. Leitura de um Item da Matriz
# =============================================================================

# 1a. leitura de um numero
print('1a:') 
numero_32 = matriz[0][1]
print(numero_32)


# 1b. leitura de um numero 
print('1b:')
numero_65 = matriz[1][2]
print(numero_65)


# 1c. leitura de um numero 
# numero_65 = A[1, 2]    (NAO É VALIDO)
#  --> TypeError: list indices must be integers or slices, not tuple


# =============================================================================
#  2. Leitura de linha
# =============================================================================

# 2a. leitura de uma linha inteira
print('2a:')
linha_0 = matriz[0]
print(linha_0)


# 2b. leitura de parte de uma linha
print('2b:')
linha_0 = matriz[0][1:3]
print(linha_0)


# (ERRADO) 2c. leitura de uma coluna (Nao retorna o que voce espera)
print('3a:')
coluna_0 = matriz[0:2][0]
print(coluna_0)
coluna_1 = matriz[0:2][1]
print(coluna_1)


# =============================================================================
#  3. Leitura de Coluna
# =============================================================================

# 3b. leitura de uma coluna
print('3b:')
coluna_0 = [linha[0] for linha in matriz]
print(coluna_0)
coluna_1 = [linha[1] for linha in matriz]
print(coluna_1)