# Análise Exploratória: Dataset Sirtuin6 Small Molecules

## 1. Estrutura dos Dados

O dataset consiste em 100 instâncias e 7 colunas, sendo 6 variáveis contínuas e 1 variável categórica (`Class`). As variáveis contínuas representam descritores moleculares que são usados para classificar as moléculas em dois grupos: `High_BFE` e `Low_BFE`.

## 2. Estatísticas Descritivas

As estatísticas descritivas para as variáveis contínuas estão resumidas na tabela abaixo:

| **Variável** | **Média** | **Desvio Padrão** | **Mínimo** | **1º Quartil** | **Mediana** | **3º Quartil** | **Máximo** |
|--------------|-----------|-------------------|------------|----------------|-------------|----------------|------------|
| **SC-5**     | 0.420     | 0.195             | 0.083      | 0.282          | 0.393       | 0.533          | 0.919      |
| **SP-6**     | 4.429     | 1.403             | 2.092      | 3.345          | 4.107       | 5.303          | 7.642      |
| **SHBd**     | 0.357     | 0.339             | 0.000      | 0.000          | 0.373       | 0.483          | 1.465      |
| **minHaaCH** | 0.444     | 0.139             | 0.000      | 0.430          | 0.468       | 0.506          | 0.721      |
| **maxwHBa**  | 1.920     | 0.523             | 0.000      | 1.840          | 2.020       | 2.162          | 3.779      |
| **FMF**      | 0.376     | 0.072             | 0.154      | 0.327          | 0.376       | 0.423          | 0.537      |

## 3. Distribuição das Variáveis

- **SC-5**: A variável apresenta uma distribuição com média em torno de 0.42 e um desvio padrão de 0.195. A maioria dos valores se concentra entre 0.282 e 0.533.
- **SP-6**: Com média de 4.43 e desvio padrão de 1.403, a distribuição é mais dispersa, variando de 2.09 a 7.64.
- **SHBd**: Notável por ter muitos valores em zero, sugerindo que essa variável pode não estar uniformemente distribuída entre as instâncias.
- **minHaaCH**: Com valores variando de 0 a 0.721, a maioria dos valores está entre 0.43 e 0.506.
- **maxwHBa**: A distribuição é mais ampla, com um desvio padrão de 0.523.
- **FMF**: É a variável com a menor dispersão, indicando uma distribuição mais concentrada em torno da média de 0.376.

## 4. Balanceamento de Classes

O dataset classifica as moléculas em duas categorias: `High_BFE` e `Low_BFE`. É importante verificar o equilíbrio entre essas classes para garantir que os modelos de classificação não fiquem enviesados.

## 5. Correlação Entre Variáveis

Seria útil calcular a matriz de correlação entre as variáveis contínuas para entender como elas se relacionam entre si. Isso ajuda a identificar possíveis multicolinearidades.

## 6. Visualizações Sugeridas

- **Histograma**: Para cada variável contínua, plotar histogramas para entender melhor suas distribuições.
- **Boxplot**: Para identificar possíveis outliers e comparar a distribuição das variáveis entre as duas classes.
- **Pairplot**: Para visualizar as relações entre pares de variáveis e como elas diferem entre as classes.
- **Heatmap de Correlação**: Para visualizar a correlação entre as variáveis.

## 7. Considerações Finais

Os dados parecem ser bem comportados, sem valores ausentes e com uma variação significativa entre as variáveis. A análise mais detalhada, especialmente com visualizações, pode fornecer mais insights sobre como essas variáveis se comportam em relação à classificação das moléculas.
