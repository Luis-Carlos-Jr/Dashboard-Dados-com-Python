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
print(data_frame.describe(include='object'))

