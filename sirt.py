import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def make_np_array(dataframe):
    columns = {}
    
    for column in dataframe.columns:
        array = []

        for index, row in dataframe.iterrows():
            array.append(row[column])

        if len(array) > 0: 
            columns[column] = np.array(array)

    return columns
    
def generate_correlation_matrix(dict):
    data_matrix = np.array([dict[key] for key in dict])
    correlation_matrix = np.corrcoef(data_matrix)
    return correlation_matrix

def plot_corr_matrix(corr_matrix):
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.show()

def plot_hist(dataframe):
    for column in df_mols:
        plt.figure()
        dataframe[column].hist(bins=30, edgecolor="black")
        plt.title(f"Histograma de {column}")
        plt.xlabel(column)
        plt.ylabel("Frequência")
        plt.show()

df = pd.read_csv(r"./data/SIRTUIN6.csv")

df_class = df["Class"]
df_mols = df.drop("Class", axis=1)

#Medidas de tendencia central
print(df_mols.describe())

np_array = make_np_array(df_mols)
corr_matrix = generate_correlation_matrix(np_array)
plot_corr_matrix(corr_matrix)
plot_hist(df_mols)
