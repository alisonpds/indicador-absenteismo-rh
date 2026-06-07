import pandas as pd
import random
from faker import Faker
from pathlib import Path
from datetime import timedelta
fake = Faker('pt_BR')

# ==========================
# Configurações
# ==========================
TOTAL_AUSENCIAS = 3000
tipos_ausencia = [
    'Atestado Médico',
    'Falta Injustificada',
    'Acompanhamento Médico',
    'Acidente de Trabalho',
    'Licença Médica'
]
cids = [
    'J11',   # Gripe
    'M54',   # Dor lombar
    'F41',   # Ansiedade
    'F32',   # Depressão
    'A09',   # Gastroenterite
    'R51',   # Cefaleia
    'B34',   # Infecção viral
    'Z76',   # Consulta médica
    'S93',   # Entorse
    'T14'    # Lesão
]
dados = []

# ==========================
# Distribuição Realista
# ==========================
for i in range(TOTAL_AUSENCIAS):
    colaborador = random.randint(1, 500)
    data_inicio = fake.date_between(
        start_date='-3y',
        end_date='today'
    )
    tipo = random.choices(
        population=tipos_ausencia,
        weights=[55, 10, 15, 5, 15],
        k=1
    )[0]
    if tipo == 'Falta Injustificada':
        dias = 1
    elif tipo == 'Acompanhamento Médico':
        dias = random.randint(1, 2)
    elif tipo == 'Atestado Médico':
        dias = random.randint(1, 5)
    elif tipo == 'Licença Médica':
        dias = random.randint(5, 30)
    else:
        dias = random.randint(2, 15)
    data_fim = data_inicio + timedelta(days=dias)
    horas_perdidas = dias * 8
    cid = random.choice(cids)
    dados.append({
        'id_colaborador': colaborador,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'dias_afastamento': dias,
        'horas_perdidas': horas_perdidas,
        'tipo_ausencia': tipo,
        'cid': cid
    })

# ==========================
# DataFrame
# ==========================
df = pd.DataFrame(dados)

# ==========================
# Salvar CSV
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent
arquivo = BASE_DIR / 'data' / 'ausencias.csv'
df.to_csv(
    arquivo,
    sep=';',
    index=False,
    encoding='utf-8-sig'
)
print(df.head())
print('\nQuantidade de registros:')
print(len(df))
print(f'\nArquivo salvo em:\n{arquivo}')