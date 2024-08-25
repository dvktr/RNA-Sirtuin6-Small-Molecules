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

## 3. Matriz de Correlação

### Tabela
|            | SC-5   | SP-6   | SHBd   | minHaaCH | maxwHBa | FMF    |
|------------|--------|--------|--------|----------|---------|--------|
| **SC-5**   | 1.000  | 0.662  | -0.102 | 0.110    | -0.084  | 0.182  |
| **SP-6**   | 0.662  | 1.000  | -0.113 | 0.196    | 0.090   | 0.580  |
| **SHBd**   | -0.102 | -0.113 | 1.000  | 0.233    | 0.049   | 0.053  |
| **minHaaCH**| 0.110 | 0.196  | 0.233  | 1.000    | 0.461   | 0.258  |
| **maxwHBa**| -0.084 | 0.090  | 0.049  | 0.461    | 1.000   | 0.190  |
| **FMF**    | 0.182  | 0.580  | 0.053  | 0.258    | 0.190   | 1.000  |

### Imagem
![Matriz de Correlação](https://github.com/user-attachments/assets/ffced4f6-3e16-414f-b309-99c85a016ecb)

## 4. Histograma de cada variável

### SC-5
![image](https://github.com/user-attachments/assets/cd787567-3ac1-4c6f-86ef-57c94591a8a5)

### SP-6
![image](https://github.com/user-attachments/assets/6214942a-7b36-4ba1-a663-9b95ed3adaf4)

### SHBd
![image](https://github.com/user-attachments/assets/566b0f0e-9430-4ca4-85ff-ce6b429d4d3b)

### minHaaCH
![image](https://github.com/user-attachments/assets/5b7a6fb1-2548-40a8-982c-b6dc8dc4b769)

### maxwHBa
![image](https://github.com/user-attachments/assets/4ad33be1-9ace-45fc-bf29-50dd89739203)

### FMF
![image](https://github.com/user-attachments/assets/f43e90f5-c75a-4bff-8c3f-4fd6f08a5bae)
