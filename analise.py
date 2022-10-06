import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


df =  pd.read_excel('C:/Users/paulo.barroz/Desktop/bootcamp_python_dio/pandas/Cusro_Python_Pandas_Digital_Innovation-master/datasets/AdventureWorks.xlsx')

print(df.head())
print('\n')

#quantidade de linhas e colunas
print('quantidade de linhas e colunas')
print(df.shape)

#Verificando os tipos de datos
print('Verificando os tipos de datos')
print(df.dtypes)

#receita total
print('Receita total')
print(df['Valor Venda'].sum())

#qual custo total?
print('adicionando a colunas custo')
df['custo'] = df['Custo Unitário'].mul(df['Quantidade'])
print(df.head(1))

print('calculando o custo e arrendodando')
print(round(df['custo'].sum(),2))

#agora vamos achar o lucro
print('coluna lucro')
df['Lucro'] = df['Valor Venda'] - df['custo']
print(df.head(1))

#lucro
print('Lucro total da empresa')
print(round(df['Lucro'].sum(),2))

#tempo de envio
print('Gerando a qtd de dias de envio de vendas')
df['tempo de envio'] = df['Data Envio'] - df['Data Venda']
print(df.head())

#extraindo apenas os  dias
print('transformando tempo envio em numero extraindo somente os dias')
df['tempo de envio'] = (df['Data Envio'] - df['Data Venda']).dt.days
print(df.head())

print(df['tempo de envio'].dtype)

#media do tempo de envio por marca
print('agrupando dados com a media ')
print(df.groupby('Marca')['tempo de envio'].mean())

#verificando se temos dados nulos
print('verificando se temos dados faltando')
print(df.isnull().sum())

#vamos agrupar lucro por ano e por marca
print('agrupando por ano e por marca')
print(df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum())

pd.options.display.float_format = "{:20,.2f}".format

#resentando o index
Lucro_ano =  df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum().reset_index()
print(Lucro_ano)

#qual total de produtos vendidos?
print(df.groupby('Produto')['Quantidade'].sum().sort_values(ascending = False))

#grafico total de produtos vendidos

#df.groupby('Produto')['Quantidade'].sum().sort_values(ascending = True).plot.barh(title = 'total de produtos vendidos')
##plt.xlabel('Total')
#plt.ylabel('Produto')
#plt.show()

##df.groupby(df['Data Venda'].dt.year)['Lucro'].sum().plot.bar(title= 'Lucro x Ano')
##plt.xlabel('Ano')
##plt.ylabel('Receita');
##plt.show()

print(df.groupby(df['Data Venda'].dt.year)['Lucro'].sum())

## venda apenas do ano de 2009

df_2009 = df[df['Data Venda'].dt.year == 2009]

print(df_2009.head())

## graficos com mes ano 2009
df_2009.groupby(df_2009['Data Venda'].dt.month)['Lucro'].sum().plot(title = 'Lucro x mes')
plt.xlabel('Mes')
plt.ylabel('Lucro')
plt.show()

df_2009.groupby('Marca')['Lucro'].sum().plot.bar(title= 'Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('lucro')
plt.xticks(rotation= 'horizontal')
plt.show()