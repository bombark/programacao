


# Aula 20 - Matrizes

## 0. Introdução

Requisitos da Aula:
- Saber comandos de atribuiçao
- Saber comandos de repetição: While e For
- Saber Iteradores
- Saber Listas

Depois da Aula:
- Saber a organização de uma Matriz na Mémoria
  - Saber a diferença entre as Matrizes do Numpy e as Matrizes Nativas
- Poder instanciar uma Matriz
- Poder acessar e alterar valores de uma Matriz
- Poder mostrar uma Matriz
- Poder iterar uma Matriz
- Poder realizar multiplicação matricial sobre Matrizes Numpy
- Poder resolver sistemas de equação sobre Matrizes Numpy

## 1a. Matrizes Nativas em Python

```python
matriz = [
    [16, 32, 64]
    [17, 33, 65]
    [18, 34, 66]
]
```

```
Matriz A : 7792365acb40
7792365acb40  01 00 00 00 00 00 00 00  a0 b8 a3 00 00 00 00 00  |................|
7792365acb50  05 00 00 00 00 00 00 00  d0 d4 34 36 92 77 00 00  |..........46.w..|
7792365acb60  06 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
7792365acb70  70 54 5d 36 92 77 00 00  b0 37 5b 36 92 77 00 00  |pT]6.w...7[6.w..|
7792365acb80  01 00 00 00 00 00 00 00  a0 b8 a3 00 00 00 00 00  |................|
7792365acb90  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
7792365acba0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
7792365acbb0  ff ff ff ff 00 00 00 00  c0 72 a4 00 00 00 00 00  |.........r......|
```

## 1b. Exemplos

- Exemplos de instanciação de matrizes
- Exemplos de como iterar uma matriz
- Exemplos de como mostrar uma matriz
- Exemplos de acesso a matriz


## 2a. Matrizes usando Numpy

O principal motivo para a popularidade do NumPy é sua eficiência e velocidade, especialmente quando comparado às listas padrão do Python. O NumPy atinge essa performance por meio de seu objeto principal: o ndarray (N-dimensional array).

Arrays Multidimensionais (ndarray): O ndarray é uma estrutura de dados de alta performance que armazena elementos do mesmo tipo de dado em um bloco de memória contíguo. Isso permite que o processador do seu computador acesse e processe os dados de forma muito mais rápida. Ao contrário de uma lista Python, onde cada elemento pode ser de um tipo diferente e estar espalhado na memória, um ndarray é otimizado para operações matemáticas.

Operações Vetorizadas: O NumPy permite realizar operações matemáticas em arrays inteiros de uma vez, sem a necessidade de loops explícitos. Essa abordagem, conhecida como vetorização, é executada em código C/Fortran otimizado por baixo dos panos. Isso não apenas acelera drasticamente os cálculos, mas também torna o código mais limpo, conciso e fácil de ler.

Ampla Gama de Funções Matemáticas: Além dos arrays, o NumPy oferece uma coleção vasta de funções matemáticas de alto nível para trabalhar com esses arrays, incluindo:

- Álgebra Linear: Funções para produto de matrizes, cálculo de determinantes, autovalores e autovetores, resolução de sistemas de equações e muito mais.
- Estatística: Funções para calcular média, mediana, desvio padrão, variância, etc.
- Transformada de Fourier
- Números Aleatórios


## 2b. Exemplos

- Exemplos de instanciação de matrizes numpy
- Exemplos de como realizar operações sobre matrizes numpy
- Exemplos de como resolver sistemas de equações usando matrizes numpy


