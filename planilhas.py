import pandas as pd
import pvlib
import matplotlib.pyplot as plt

## leitura de arquivos
df1 =  pd.read_excel('C:/Users/paulo.barroz/Desktop/bootcamp_python_dio/pandas/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Aracaju.xlsx')
df2 =  pd.read_excel('C:/Users/paulo.barroz/Desktop/bootcamp_python_dio/pandas/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Fortaleza.xlsx')
df3 =  pd.read_excel('C:/Users/paulo.barroz/Desktop/bootcamp_python_dio/pandas/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Natal.xlsx')
df4 =  pd.read_excel('C:/Users/paulo.barroz/Desktop/bootcamp_python_dio/pandas/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Recife.xlsx')
df5 =  pd.read_excel('C:/Users/paulo.barroz/Desktop/bootcamp_python_dio/pandas/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Salvador.xlsx')

#print(df1.head(5))

#jutando os arquivos
df = pd.concat([df1,df2,df3,df4,df5])

#Exibindo as 5 primeiras linhas
#print(df.head(5))
#print(df.dtypes)
#print('\n')

#verificar valores nulos
#print(df.isnull().sum())

#criando uma nova coluna
#print(df.head())
#df = df['receita'] = df['Vendas'].mul(df['Qtde'])
#print(df.head())

#retornando maior receita
#print(df['receita'].max())
#retornando menor receita
#print(df['receita'].min())

#nlargest retorna o top 3 com base em uma coluna
#print(df.nlargest(3, 'receita'))
#nlargest retorna o top 3 ruim  com base em uma coluna
#print(df.nsmallest(3,'receita'))

#agrupamento por cidade
#print(df.groupby('Cidade')['receita'].sum())

#ordernando o conjunto de dados
#print(df.sort_values('receita', ascending=False).head(10))

## transformando coluna data em inteirno
#df['Data'] = df['Data'].astype("int64")
#print(df.dtypes)

##transformando coluna em data
#df['Data'] = pd.to_datetime(df['Data'])
#print(df.dtypes)

#agrupamento por ano
print(df.head())


print(df['LojaID'].value_counts(ascending = False))

#gragico de barras
#print(df['LojaID'].value_counts(ascending = False).plot.bar())
#plt.show()
#print(df['LojaID'].value_counts(ascending = False).plot.barh())##horizontais sem ordem 
##plt.show()
#print(df['LojaID'].value_counts(ascending = True).plot.barh())##horizontais com ordem 
#plt.show()

#grafico de pizza

# total de venda spor cidade
##print(df['Cidade'].value_counts().plot.bar(title = 'Quantidade  de pedidos por cidade'))
#plt.xlabel('Cidade')
#plt.ylabel('total de pedidos')
#plt.show()

# total de venda spor cidade grafico
#print(df['Cidade'].value_counts().plot.bar(title = 'Quantidade  de pedidos por cidade', color = 'green'))
##plt.xlabel('Cidade')
##plt.ylabel('total de pedidos')
##plt.show()

print(df.groupby(df['mes_venda'])['Qtde'].sum().plot())
