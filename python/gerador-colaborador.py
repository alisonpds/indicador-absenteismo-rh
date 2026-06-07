import pandas as pd
import random
from faker import Faker
from pathlib import Path
fake = Faker('pt_BR')

# =========================
# Estrutura Organizacional
# =========================
estrutura = {
    'Produção': {
        'gestor': 'Ricardo Almeida',
        'cargos': [
            'Assistente',
            'Analista Jr',
            'Analista Pleno',
            'Supervisor'
        ]
    },
    'Logística': {
        'gestor': 'Ricardo Almeida',
        'cargos': [
            'Assistente',
            'Analista Jr',
            'Analista Pleno',
            'Supervisor'
        ]
    },
    'Comercial': {
        'gestor': 'Fernanda Souza',
        'cargos': [
            'Assistente',
            'Analista Jr',
            'Analista Pleno',
            'Analista Sênior',
            'Coordenador'
        ]
    },
    'Financeiro': {
        'gestor': 'Carlos Henrique',
        'cargos': [
            'Assistente',
            'Analista Jr',
            'Analista Pleno',
            'Analista Sênior',
            'Especialista',
            'Coordenador'
        ]
    },
    'Recursos Humanos': {
        'gestor': 'Patricia Martins',
        'cargos': [
            'Assistente',
            'Analista Jr',
            'Analista Pleno',
            'Analista Sênior',
            'Especialista'
        ]
    },
    'Tecnologia': {
        'gestor': 'Juliana Costa',
        'cargos': [
            'Analista Jr',
            'Analista Pleno',
            'Analista Sênior',
            'Especialista',
            'Coordenador'
        ]
    },
    'Qualidade': {
        'gestor': 'Juliana Costa',
        'cargos': [
            'Assistente',
            'Analista Jr',
            'Analista Pleno',
            'Supervisor'
        ]
    }
}

# =========================
# Distribuição por Área
# =========================
areas_distribuidas = (
        ['Produção'] * 180 +
        ['Logística'] * 80 +
        ['Comercial'] * 70 +
        ['Tecnologia'] * 60 +
        ['Financeiro'] * 40 +
        ['Recursos Humanos'] * 30 +
        ['Qualidade'] * 40
)
random.shuffle(areas_distribuidas)
dados = []
for i in range(1, 501):
    area = areas_distribuidas[i - 1]
    gestor = estrutura[area]['gestor']
    cargo = random.choice(
        estrutura[area]['cargos']
    )
    data_nascimento = fake.date_of_birth(
        minimum_age=18,
        maximum_age=60
    )
    data_admissao = fake.date_between(
        start_date='-10y',
        end_date='today'
    )
    dados.append({
        'matricula': f'MAT{i:04}',
        'nome': fake.name(),
        'sexo': random.choice([
            'Masculino',
            'Feminino'
        ]),
        'data_nascimento': data_nascimento,
        'area': area,
        'cargo': cargo,
        'gestor': gestor,
        'data_admissao': data_admissao,
        'status': 'Ativo'
    })

# =========================
# DataFrame
# =========================
df = pd.DataFrame(dados)

# =========================
# Salvar CSV na pasta data
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
arquivo = BASE_DIR / 'data' / 'colaboradores.csv'
arquivo.parent.mkdir(
    parents=True,
    exist_ok=True
)
df.to_csv(
    arquivo,
    sep=';',
    index=False,
    encoding='utf-8-sig'
)

# =========================
# Validação
# =========================
print(df.head())
print('\nQuantidade de colaboradores:')
print(len(df))
print('\nColaboradores por área:')
print(df['area'].value_counts())
print(f'\nArquivo salvo em:\n{arquivo}')