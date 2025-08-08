## Enunciado: Jogo da Vida de Conway

Crie um programa em Python que simule o **Jogo da Vida de Conway**.

### Descrição do Jogo

O Jogo da Vida é um autômato celular, um modelo matemático que simula a evolução de uma população de células em uma grade bidimensional. O jogo se desenrola em um tabuleiro infinito (para simplificar, usaremos um tabuleiro finito com bordas fixas) onde cada célula pode estar em um de dois estados: **viva** ou **morta**. A evolução do jogo é determinada por um conjunto de regras simples, aplicadas a cada célula em cada geração (ou passo de tempo):

1.  **Sobrevivência**: Uma célula viva com 2 ou 3 vizinhos vivos sobrevive para a próxima geração.
2.  **Morte por solidão**: Uma célula viva com menos de 2 vizinhos vivos morre.
3.  **Morte por superpopulação**: Uma célula viva com mais de 3 vizinhos vivos morre.
4.  **Nascimento**: Uma célula morta com exatamente 3 vizinhos vivos se torna uma célula viva.

Um **vizinho** é qualquer uma das 8 células adjacentes (horizontal, vertical e diagonal).

### Requisitos do Exercício

1.  **Representação do Tabuleiro**: Represente o tabuleiro como uma lista de listas (ou uma matriz) em Python. As células vivas podem ser representadas por `1` e as células mortas por `0`.

2.  **Configuração Inicial**: O programa deve começar com uma configuração inicial de células vivas. Você pode codificar um padrão inicial ou ler de um arquivo. Exemplo de um padrão simples é o "glider":

    ```python
    glider = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]
    ```

3.  **Função para Contar Vizinhos**: Crie uma função que receba a posição de uma célula `(x, y)` e o tabuleiro atual, e retorne o número de vizinhos vivos dessa célula. Tenha cuidado com as bordas do tabuleiro para evitar erros de índice.

4.  **Função para Evoluir o Tabuleiro**: Crie uma função principal que implemente a lógica do jogo. Essa função deve gerar um novo tabuleiro a partir do estado atual, aplicando as 4 regras a cada célula. **Importante**: Todas as regras devem ser aplicadas simultaneamente. Isso significa que a decisão sobre o estado de uma célula na próxima geração deve ser baseada apenas no estado da geração atual. Use um novo tabuleiro temporário para armazenar o próximo estado e só o substitua no final da iteração.

5.  **Exibição na Tela**: A cada iteração (geração), imprima o tabuleiro na tela de forma clara. Por exemplo, você pode usar caracteres como `█` para células vivas e `     ` para células mortas. Limpe a tela a cada nova geração para que a simulação seja fluida. Você pode usar a biblioteca `os` para isso, com `os.system('cls')` no Windows ou `os.system('clear')` no Linux/macOS.

6.  **Loop Principal**: O programa deve rodar em um loop que avança a simulação a cada segundo (use a função `time.sleep()`). O usuário deve poder interromper o programa, por exemplo, pressionando `Ctrl+C`.

-----

### Desafios Adicionais (Opcional)

  * **Entrada do Usuário**: Permita que o usuário defina o tamanho do tabuleiro e a quantidade de gerações a serem simuladas.
  * **Padrões Pré-definidos**: Implemente a opção de carregar diferentes padrões iniciais, como "pulsar" ou "nave espacial".
  * **Bordas Cíclicas**: Em vez de bordas fixas, implemente um tabuleiro "cíclico" onde as bordas se conectam. Ou seja, a célula na borda direita é vizinha da célula na borda esquerda, e a célula na borda superior é vizinha da célula na borda inferior.