# Exemplos de Iteração sobre uma Matriz Nativa

matriz = [ 
    [16,32,64], 
    [17,33,65], 
    [18,34,66]
]


# 1. Iterando diretamente linhas e colunas
print('1:')
for linha in matriz:
    for coluna in linha:
        print(coluna, end=', ')
    print()
print()


# 2. Iterando usando indices
print('2:')
for i in range( len(matriz) ):
    for j in range( len(matriz[i]) ):
        print( matriz[i][j], end=', ')
    print()
print()


# 3. Iterando parte da matriz usando indices
print('3:')
for i in range( 1, len(matriz) ):
    for j in range( len(matriz[i]) ):
        print( matriz[i][j], end=', ')
    print()
print()