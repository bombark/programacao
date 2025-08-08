# Exemplos de Instanciação de Matriz Nativa

# 1. Tudo na mesma linha
A = [ [16,32,64] , [16,32,64] , [16,32,64]  ]


# 2. Em diferentes linhas 
A = [ 
    [16,32,64], 
    [16,32,64], 
    [16,32,64],
]


# 3. A ultima virgula é opcional
A = [ 
    [16,32,64], 
    [16,32,64], 
    [16,32,64]
]


# 4. Usando umm padrão diferente para a virgula
A = [ 
    [16,32,64] 
    , [16,32,64]
    , [16,32,64]
]


# 5. Com diferentes niveis de identação - Não é aconselhavel mas é aceito pelo python3
A = [ 
    [16,32,64], 
        [16,32,64],
            [16,32,64]
]


# 6. Cada linha com tamanhos diferentes
A = [ 
    [16], 
    [16,32],
    [16,32,64]
]


# 7. Itens com tipos diferentes
A = [
    [16, 'string', 10.5555], 
    [16, 10.5555, 'string'],
    ['string', 10.5555, 64]
]


# 8. Mostrar uma matriz
print(A)


# Instanciando usando laço de repetição na mesma linha
linhas = 3
colunas = 4
matriz = [ [0 for _ in range(colunas) ] for _ in range(linhas) ]


# =============================================================================
# Possiveis Erros
# =============================================================================

# e1) Falta uma virgula entre as listas
# SyntaxWarning: list indices must be integers or slices, not tuple; 
# perhaps you missed a comma?
#   [16, 32, 64]

# e2) Falta fechar um ]
#    A = [
#        ^
# SyntaxError: '[' was never closed

