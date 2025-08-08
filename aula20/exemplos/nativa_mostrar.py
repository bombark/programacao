# Mostrar uma Matriz

# 0. Instanciando uma matrix

A = [
    [1.23456, 7.89123, 4.56789],
    [9.01234, 5.67890, 2.34567],
    [3.45678, 6.78901, 8.90123]
]


# 1
print('1. usando o print')
print(A)
print()


# 2a
print('2a. usando laço de repeticao')
for linha in A:
    for coluna in linha:
        print(coluna, end=', ')
    print()
print()


# 2b
print('2b. usando laço de repeticao com formatação')
for linha in A:
    for coluna in linha:
        print(f"{coluna:.2f}", end="  ")
    print()
print()