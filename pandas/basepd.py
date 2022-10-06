from itertools import groupby
import pandas as pd

df = pd.read_csv("C:/Users/paulo.barroz/Desktop/bootcamp python dio/pandas/Gapminder.csv", sep=";")





df = df.rename(columns={'country':'pais','continent':'continente','year':'ano','lifeExp':'expectativa de vida','pop':'pop total','gdpPercap':'pib'})

#print(df.head(5)) ## imprimi as primeiras 5 linha da planilha

#print('\n \n \n')

#print(df.shape) ## total de linhas e colunas

#print(df.columns) # imprimi as colunas da planilha

#print(df.dtypes)## cada coluna e com sua especifição

#print(df.tail(15))

#print(df.describe())

#print(df['continente'].unique()) ## busca os valores unicos de uma coluna

#Oceania = df.loc[df['continente'] == 'Oceania'] ## filtra por oceania

#print(Oceania.head()) 

#print(df.groupby('continente')['pais'].nunique())

print(df.groupby('ano')['expectativa de vida'].mean())
