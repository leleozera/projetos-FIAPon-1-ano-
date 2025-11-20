import sqlite3
import pandas as pd
from datetime import date

# Conecta/cria BD local
conn = sqlite3.connect("dados/Globalsolutions.db")
cursor = conn.cursor()

# Criação das tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id_funcionario INTEGER PRIMARY KEY,
    cargo TEXT,
    idade INTEGER,
    tempo_empresa_anos REAL,
    trabalho_remoto INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bem_estar_diario (
    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
    id_funcionario INTEGER,
    data_registro TEXT,
    horas_trabalhadas_semanais REAL,
    humor_diario REAL,
    pontuacao_engajamento REAL,
    faltas_3_meses INTEGER,
    recebeu_treinamento_bemestar INTEGER,
    risco_burnout_previsto INTEGER,
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario)
);
""")

conn.commit()

# Importa o CSV e joga no banco (funcionários + bem-estar do "dia")
df = pd.read_csv("dados/dados_bem_estar.csv")

# Insere na tabela funcionarios
func_cols = ["id_funcionario", "cargo", "idade", "tempo_empresa_anos", "trabalho_remoto"]
df_func = df[func_cols].drop_duplicates(subset=["id_funcionario"])

df_func.to_sql("funcionarios", conn, if_exists="replace", index=False)

# Simulação: usa os dados como se fossem do dia de hoje
hoje = date.today().isoformat()

df_bem_estar = df.copy()
df_bem_estar["data_registro"] = hoje
df_bem_estar.rename(columns={"risco_burnout": "risco_burnout_previsto"}, inplace=True)

cols_bem_estar = [
    "id_funcionario",
    "data_registro",
    "horas_trabalhadas_semanais",
    "humor_diario",
    "pontuacao_engajamento",
    "faltas_3_meses",
    "recebeu_treinamento_bemestar",
    "risco_burnout_previsto"
]

df_bem_estar[cols_bem_estar].to_sql("bem_estar_diario", conn, if_exists="replace", index=False)

print("Banco Globalsolutions.db populado com dados iniciais.")

conn.close()
