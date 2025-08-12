# =========  AULA 2 - CONHECENDO OS DADOS E A BIBLIOTECA PANDAS =============
import numpy as np
import pandas

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
    "EX": "Diretoria/Executivo"
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

# Aplicar traduções
data_frame["senioridade"] = data_frame["senioridade"].replace(senioridade)
data_frame["contrato"] = data_frame["contrato"].replace(contrato)
data_frame["porte_empresa"] = data_frame["porte_empresa"].replace(porte)

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
    'temperatura':[30,np.nan,np.nan,28,27],
})

#preenchendo valores vazios com o valor do registro anterior e posterior
df_temperatura['preenchido_ffill'] = df_temperatura['temperatura'].ffill() #anterior
df_temperatura['preenchido_bfill'] = df_temperatura['temperatura'].bfill() #posterior
#print(df_temperatura)


#data frame: cidades
df_cidades = pandas.DataFrame({
    'nome':['Ana','Brunos','Carlos','Daniele','Val'],
    'cidades':['São Paulo', np.nan, 'Curitiba', np.nan, 'Belem']
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