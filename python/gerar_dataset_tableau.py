import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# ==========================================
# Conexão PostgreSQL
# ==========================================

USUARIO = "alison"
SENHA = "SUA_SENHA"
HOST = "localhost"
PORTA = "5432"
BANCO = "absenteismo"

engine = create_engine(
    f"postgresql+psycopg2://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"
)

# ==========================================
# Ler tabelas
# ==========================================

colaboradores = pd.read_sql(
    "SELECT * FROM colaboradores",
    engine
)

ausencias = pd.read_sql(
    "SELECT * FROM ausencias",
    engine
)

# ==========================================
# JOIN
# ==========================================

df = colaboradores.merge(
    ausencias,
    on="id_colaborador",
    how="inner"
)

# ==========================================
# Idade
# ==========================================

hoje = pd.Timestamp.today()

df["idade"] = (
    (hoje - pd.to_datetime(df["data_nascimento"]))
    .dt.days // 365
)

# ==========================================
# Faixa Etária
# ==========================================

df["faixa_etaria"] = pd.cut(
    df["idade"],
    bins=[18, 25, 35, 45, 55, 100],
    labels=[
        "18-24",
        "25-34",
        "35-44",
        "45-54",
        "55+"
    ],
    right=False
)

# ==========================================
# Geração
# ==========================================

ano_nascimento = pd.to_datetime(
    df["data_nascimento"]
).dt.year

df["geracao"] = "Geração Z"

df.loc[
    ano_nascimento.between(1981, 1996),
    "geracao"
] = "Millennial"

df.loc[
    ano_nascimento.between(1965, 1980),
    "geracao"
] = "Geração X"

df.loc[
    ano_nascimento <= 1964,
    "geracao"
] = "Baby Boomer"

# ==========================================
# Categoria CID
# ==========================================

def categoria_cid(cid):

    if cid in ["F32", "F41"]:
        return "Saúde Mental"

    elif cid in ["J11", "B34"]:
        return "Respiratório"

    elif cid in ["M54", "S93", "T14"]:
        return "Ortopédico"

    elif cid == "A09":
        return "Gastrointestinal"

    else:
        return "Outros"


df["categoria_cid"] = (
    df["cid"]
    .apply(categoria_cid)
)

# ==========================================
# Recorrência
# ==========================================

recorrencia = (
    df.groupby("id_colaborador")
      .size()
      .reset_index(name="qtd_ausencias")
)

df = df.merge(
    recorrencia,
    on="id_colaborador"
)

df["recorrente"] = (
    df["qtd_ausencias"]
      .apply(
        lambda x:
        "Recorrente"
        if x >= 5
        else "Não Recorrente"
    )
)

# ==========================================
# Ano / Mês
# ==========================================
df["ano_mes"] = pd.to_datetime(
    df["data_inicio"]
).dt.to_period("M").dt.to_timestamp()

# ==========================================
# Exportar Tableau
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

arquivo = (
    BASE_DIR
    / "data"
    / "absenteismo_dashboard.csv"
)

df.to_csv(
    arquivo,
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("=" * 50)
print("DATASET TABLEAU GERADO")
print("=" * 50)

print(f"Registros: {len(df):,}")
print(f"Colunas: {len(df.columns)}")

print(f"\nArquivo:\n{arquivo}")