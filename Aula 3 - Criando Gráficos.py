# =========  AULA 2 - CONHECENDO OS DADOS E A BIBLIOTECA PANDAS =============
from random import betavariate

import pandas
from matplotlib import pyplot as plt
from seaborn import kdeplot
from setuptools.monkey import patch_all

#lendo a base de dados
data_frame = pandas.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
data_frame.head() #exibir as 5 primeiras linhas da tabela
#print(data_frame.head())

#data_frame.info() #exibindo informações da tabela

data_frame.describe() #exibindo descrição dos dados
#print(data_frame.describe())

data_frame.shape #exibir o tamanho da base (linhas, colunas)
#print(data_frame.shape)
linhas, colunas = data_frame.shape[0], data_frame.shape[1]
#print('Número de linhas: ', linhas)
#print('Número de colunas: ', colunas)

#exibindo os nomes das colunas
data_frame.columns
#print(data_frame.columns)

#renomeando as colunas para PT-BR
# Criar o mapeamento de nomes
colunas = {
    "work_year": "ano",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda",
    "salary_in_usd": "usd",
    "employee_residence": "residencia",
    "remote_ratio": "remoto",
    "company_location": "empresa",
    "company_size": "porte_empresa"
}

# Renomear colunas
data_frame.rename(columns=colunas, inplace=True)

# Verificar resultado
#print(data_frame.head())

# Tradução de valores categóricos
senioridade = {
    "EN": "Júnior",
    "MI": "Pleno",
    "SE": "Sênior",
    "EX": "Executivo"
}

contrato = {
    "PT": "Meio Período",
    "FT": "Tempo Integral",
    "CT": "Contrato",
    "FL": "Freelancer"
}

porte = {
    "S": "Pequena",
    "M": "Média",
    "L": "Grande"
}

remoto = {
    0: "Presencial",
    50: "Híbrido",
    100: "Remoto"
}

# Aplicar traduções
data_frame["senioridade"] = data_frame["senioridade"].replace(senioridade)
data_frame["contrato"] = data_frame["contrato"].replace(contrato)
data_frame["porte_empresa"] = data_frame["porte_empresa"].replace(porte)
data_frame["remoto"] = data_frame["remoto"].replace(remoto)

# Exibir resultado
#print(data_frame.head())

#exibindo a frequência de ocorrências de algumas informações
data_frame['senioridade'].value_counts()
#print(data_frame['senioridade'].value_counts())
data_frame['remoto'].value_counts()
#print(data_frame['senioridade'].value_counts())
data_frame['remoto'].value_counts()
#print(data_frame['porte_empresa'].value_counts())
data_frame['remoto'].value_counts()
#print(data_frame['senioridade'].value_counts())

#print(data_frame.head())

#exibindo informações de ocorrencias de colunas incluindo não númericas
#print(data_frame.describe(include='object'))

# =========  AULA 2 - TRATAMENTO DE DADOS =============

import numpy

#procurando no data frame por valores nulos (não existentes)
#print(data_frame.isnull())

#fazendo contagem dos valores nulos
#print(data_frame.isnull().sum())

#verificando valores presenstes no campo 'ano'
#nan = Not a Number
#print(data_frame['ano'].unique())

#exibindo as linhas com valores nulos
#print(data_frame[data_frame.isnull().any(axis=1)])

#--- Exemplo de Criação de Data Frame ---

#data frame: salarios
df_salarios = pandas.DataFrame({
    'nome':['Ana','Brunos','Carlos','Daniele','Val'],
    'salario':[4000,numpy.nan, 5000, numpy.nan, 100000]
})

#preenchendo campos vazio com a media e a mediana dos valores validos
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
#print(df_salarios)


#data frame: Temperaturas
df_temperatura = pandas.DataFrame({
    'dia da semana':['seg','ter','qua','qui','sex'],
    'temperatura':[30,numpy.nan,numpy.nan,28,27],
})

#preenchendo valores vazios com o valor do registro anterior e posterior
df_temperatura['preenchido_ffill'] = df_temperatura['temperatura'].ffill() #anterior
df_temperatura['preenchido_bfill'] = df_temperatura['temperatura'].bfill() #posterior
#print(df_temperatura)


#data frame: cidades
df_cidades = pandas.DataFrame({
    'nome':['Ana','Brunos','Carlos','Daniele','Val'],
    'cidades':['São Paulo', numpy.nan, 'Curitiba', numpy.nan, 'Belem']
})

#preenchendo valores nulos com valores predefinidos
df_cidades['cidade_preenchida'] = df_cidades['cidades'].fillna('Não Informado')
#print(df_cidades)

#-----------------------------------------------------

#limpando dados nulos do data frame
df_limpo = data_frame.dropna()
#print(df_limpo.isnull().sum())

#validadndo formatos dos campos
#0 campo 'ano' está exibido com casas decimais
#print(df_limpo.head())

#print(df_limpo.info())

#alterar o tipo de dado do campo ano de float para int
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
#print(df_limpo.head())
#print(df_limpo.info())

#===== Aula 3 - Criando Gráficos =====
import seaborn #biblioteca para graficos estaticos
import plotly.express as px #bibliotecas para gráficos interativos

#import matplotlib.pyplot
# ao importar a biblioteca seaborn, tb é importado
#a matplotlib que é usada pela seaborn

#criando e exibindo um gráfico de barras de frequencia de senioridades
#df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de Senioridade')
#plt.show()

#montando gráfico de media de salarios por senioridade
#seaborn.barplot(data = df_limpo, x='senioridade', y='usd')
#plt.show() #plt é o apelido do modulo pyplot da biblioteca matplotlib que já foi importada assim

#customizando tamanho e títulos do gráfico
#plt.figure(figsize=(8,5))
#seaborn.barplot(data = df_limpo, x='senioridade', y='usd')
#plt.title('Salário Médio por Senioridade')
#plt.xlabel('Senioridade')
#plt.ylabel('Salário Médio Anual em USD')
#plt.show()

#criando ordenação de senioridade por média de salário em usd
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index
#print(ordem)

#criando gráfico customizado com ordenação decrescente de senioridade por média de usd
# plt.figure(figsize=(8,5))
# seaborn.barplot(data = df_limpo, x='senioridade', y='usd',order=ordem)
# plt.title('Salário Médio por Senioridade')
# plt.xlabel('Senioridade')
# plt.ylabel('Salário Médio Anual em USD')
# plt.show()

#criando gráfico customizado com ordenação crescente de senioridade por média de usd
# ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index
# plt.figure(figsize=(8,5))
# seaborn.barplot(data = df_limpo, x='senioridade', y='usd',order=ordem)
# plt.title('Salário Médio por Senioridade')
# plt.xlabel('Senioridade')
# plt.ylabel('Salário Médio Anual em USD')
# plt.show()

#criando um gráfico de histograma
# ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index
# plt.figure(figsize=(8,4)) #dimensões do gráfico
# seaborn.histplot(df_limpo['usd'],bins = 50, kde = True) #tipo do gráfico e estatística
# plt.title('Distribuição de salários anuais')
# plt.xlabel('Salário em USD ')
# plt.ylabel('Frequencia')
# plt.show()

# criando grafico do tipo boxplot
# plt.figure(figsize=(8,4))
# seaborn.boxplot(x = df_limpo['usd'])
# plt.title('Boxplot Salário')
# plt.xlabel('Salário em USD ')
# plt.show()

#criando um boxplot filtrado por senioridade
# ordem = ["Júnior",'Pleno', 'Sênior', 'Executivo']
# plt.figure(figsize = (8,5))
# seaborn.boxplot(x = 'senioridade', y = 'usd', data = df_limpo, order = ordem)
# plt.title('Distribuição salarial por senioridade')
# plt.xlabel('Salário em USD ')
# plt.show()

#colorindo um boxplot filtrado por senioridade
# ordem = ["Júnior",'Pleno', 'Sênior', 'Executivo']
# plt.figure(figsize = (8,5))
# #paleta para graficos categóricos 'Set2'
# seaborn.boxplot(x = 'senioridade', y = 'usd', data = df_limpo, order = ordem, palette = 'Set2', hue='senioridade')
# plt.title('Distribuição salarial por senioridade')
# plt.xlabel('Salário em USD ')
# plt.show()

#=========== Gráfico Interativo ===============

# ----------- Barras ----------

# # Calcula a média de salário por senioridade em gráfico de barras interativo
# media = df_limpo.groupby("senioridade", as_index=False)["usd"].mean()#.sort_values(by="usd", ascending=False)
#
# # Ordena do maior para o menor
# media = media.sort_values(by="usd", ascending=False)#.reset_index()
#
# # Cria gráfico de barras
# fig = px.bar(
#     media,
#     x="senioridade",
#     y="usd",
#     text="usd",
#     title="Média Salarial por Senioridade",
#     labels={"senioridade": "Senioridade", "usd": "Salário Médio (USD)"},
#     color="senioridade"
# )
#
# # Formata os valores no topo das barras
# fig.update_traces(texttemplate="$%{text:,.0f}", textposition="inside")
#
# fig.show()

# ----------- Pizza ----------

# # Calcula a média de salário por senioridade em gráfico de pizza interativo
# media = df_limpo.groupby("senioridade", as_index=False)["usd"].mean()#.sort_values(by="usd", ascending=False)
#
# # Ordena do maior para o menor
# media = media.sort_values(by="usd", ascending=False)#.reset_index()
#
# #
# contagem = df_limpo['remoto'].value_counts().reset_index()
# contagem.columns = ['Tipo_trabalho', 'Quantidade']
#
# # Cria gráfico de barras
# fig = px.pie(
#     contagem,
#     names = 'Tipo_trabalho',
#     values = 'Quantidade',
#     title='Porcentagem do tipo de trabalho',
#     hole=0.5
# )
# fig.update_traces(textinfo='percent+label')
# fig.show()

# ----------- Pizza filtrado ----------
#desafio de construis um gráfico de pizza de salário de cientistas de dados por país

# # Calcula a média de salário por senioridade em gráfico de pizza interativo
# media = df_limpo.groupby("senioridade", as_index=False)["usd"].mean()#.sort_values(by="usd", ascending=False)
#
# # Ordena do maior para o menor
# media = media.sort_values(by="usd", ascending=False)#.reset_index()
#
# #
# contagem = df_limpo['remoto'].value_counts().reset_index()
# contagem.columns = ['Tipo_trabalho', 'Quantidade']
#
# # Cria gráfico de barras
# fig = px.pie(
#     contagem,
#     names = 'Tipo_trabalho',
#     values = 'Quantidade',
#     title='Porcentagem do tipo de trabalho',
#     hole=0.5
# )
# fig.update_traces(textinfo='percent+label')
# fig.show()