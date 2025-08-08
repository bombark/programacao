## Enunciado: Análise de Concentração de $CO_2$ com Espectroscopia TDLAS

Crie um programa em Python que realize a análise de uma linha de absorção de $CO_2$ obtida por um dispositivo **TDLAS (Tunable Diode Laser Absorption Spectroscopy)**. O objetivo é utilizar a técnica de ajuste de curva (`curve_fit`) para modelar o perfil espectral da linha de absorção e, a partir dos parâmetros do ajuste, determinar a concentração do gás.

---

### 1. Contexto Teórico

Dispositivos TDLAS operam varrendo o comprimento de onda de um laser através de uma linha de absorção específica de um gás, como o $CO_2$. A quantidade de luz absorvida pelo gás é medida, resultando em um perfil de absorção. Para concentrações baixas a moderadas, a forma da linha de absorção pode ser bem aproximada por um **perfil de Gauss**, cuja equação é dada por:

$$A(v) = A_0 \cdot \exp \left( - \frac{(v - v_0)^2}{2\sigma^2} \right)$$

Onde:
* $A(v)$ é a absorbância medida em um dado número de onda ($v$).
* $A_0$ é a absorbância de pico (amplitude).
* $v_0$ é o número de onda central da linha de absorção.
* $\sigma$ é o desvio padrão da curva, relacionado à largura da linha.

A concentração do gás é diretamente proporcional à **área integrada sob a curva de absorção**. A área de uma função gaussiana é calculada por:

$$\text{Área} = A_0 \cdot \sigma \cdot \sqrt{2\pi}$$

O valor da concentração ($c$) é então obtido pela relação:

$$c = k \cdot \text{Área}$$

onde $k$ é uma constante de calibração que depende do dispositivo, da pressão e da temperatura. Para este exercício, você pode assumir um valor de $k = 50 \text{ ppm} \cdot \text{cm} \cdot \text{cm}^{-1}$.

### 2. Dados Fornecidos

Considere os seguintes dados de absorbância ($A$) medidos em função do número de onda ($v$) de uma linha de absorção de $CO_2$. Estes dados representam uma varredura espectral e foram gerados artificialmente para este exercício.

**Número de onda ($v$) em $cm^{-1}$:**
`v = [667.31, 667.32, 667.33, 667.34, 667.35, 667.36, 667.37, 667.38, 667.39, 667.40, 667.41, 667.42, 667.43, 667.44, 667.45]`

**Absorbância ($A$) (adimensional):**
`A = [0.005, 0.015, 0.040, 0.080, 0.150, 0.250, 0.350, 0.400, 0.350, 0.250, 0.150, 0.080, 0.040, 0.015, 0.005]`

### 3. Requisitos do Exercício

1.  **Representação dos Dados:** Armazene os dados de número de onda e absorbância em arrays NumPy.
2.  **Definição do Modelo:** Crie uma função em Python que represente o perfil gaussiano. Essa função deve receber o número de onda ($v$), a amplitude de pico ($A_0$), o número de onda central ($v_0$) e o desvio padrão ($\sigma$) como parâmetros e retornar a absorbância correspondente.
3.  **Ajuste de Curva (`curve_fit`):**
    * Utilize a função `scipy.optimize.curve_fit` para ajustar os dados fornecidos ao seu modelo gaussiano.
    * O `curve_fit` retornará os parâmetros otimizados que melhor se ajustam aos dados experimentais. Imprima os valores encontrados para $A_0$, $v_0$ e $\sigma$.
4.  **Visualização dos Resultados:**
    * Use a biblioteca `matplotlib` para criar um gráfico.
    * Plote os pontos de dados originais (Número de onda vs. Absorbância) usando um gráfico de dispersão (`scatter`).
    * No mesmo gráfico, plote a curva de melhor ajuste, gerada usando a sua função gaussiana e os parâmetros obtidos pelo `curve_fit`.
    * Adicione rótulos aos eixos, um título e uma legenda para diferenciar os dados originais da curva ajustada.
5.  **Cálculo da Concentração:**
    * Usando os parâmetros $A_0$ e $\sigma$ obtidos do ajuste, calcule a área integrada sob a curva.
    * Com a área e a constante de calibração $k$ fornecida, calcule e imprima a concentração de $CO_2$ na amostra em partes por milhão (ppm).

---

### 4. Desafios Adicionais (Opcional)

* **Implementação do Perfil de Voigt:** Para um ajuste mais preciso, substitua a função gaussiana por uma função de perfil de Voigt, que é a convolução de um perfil gaussiano e um perfil de Lorentz.
* **Adição de Ruído:** Adicione um ruído aleatório gaussiano aos dados de absorbância originais para simular dados experimentais mais realistas antes de realizar o ajuste.
* **Análise de Incertesa:** Utilize a matriz de covariância retornada pelo `curve_fit` para calcular a incerteza dos parâmetros ajustados e propagá-la para estimar a incerteza na concentração final.