import numpy as np
import pandas as pd

np.random.seed(42)  # reprodutibilidade

# Número de funcionários simulados
n = 500

# IDs
ids = np.arange(1, n + 1)

# Cargos possíveis
cargos_possiveis = ["Analista", "Desenvolvedor", "Gestor", "Estagiário", "Suporte"]

cargos = np.random.choice(cargos_possiveis, size=n, p=[0.25, 0.30, 0.15, 0.15, 0.15])

# Horas trabalhadas na semana (entre 30 e 60)
horas_trabalhadas = np.random.normal(loc=44, scale=6, size=n)
horas_trabalhadas = np.clip(horas_trabalhadas, 30, 60).round(1)

# Humor diário (média da semana) - escala 1 a 5
humor_diario = np.random.normal(loc=3.5, scale=0.8, size=n)
humor_diario = np.clip(humor_diario, 1, 5).round(1)

# Trabalho remoto (0 = presencial, 1 = remoto, 2 = híbrido)
trabalho_remoto = np.random.choice([0, 1, 2], size=n, p=[0.4, 0.3, 0.3])

# Idade
idade = np.random.randint(20, 60, size=n)

# Tempo de empresa em anos
tempo_empresa_anos = np.round(np.random.exponential(scale=3, size=n), 1)
tempo_empresa_anos = np.clip(tempo_empresa_anos, 0, 20)

# Recebeu treinamento de bem-estar (0 = não, 1 = sim)
recebeu_treinamento_bemestar = np.random.choice([0, 1], size=n, p=[0.6, 0.4])

# Pontuação de engajamento (0 a 100)
pontuacao_engajamento = np.random.normal(loc=70, scale=15, size=n)
pontuacao_engajamento = np.clip(pontuacao_engajamento, 0, 100).round(0)

# Faltas nos últimos 3 meses
faltas_3_meses = np.random.poisson(lam=1, size=n)

# Agora vamos criar o "risco de burnout" (0 = baixo, 1 = alto) com base em regras
risco_burnout_prob = (
    0.1
    + 0.02 * (horas_trabalhadas - 40)        # mais horas => mais risco
    - 0.03 * (humor_diario - 3)             # melhor humor => menos risco
    - 0.01 * (pontuacao_engajamento - 50)/10
    + 0.05 * faltas_3_meses
    - 0.05 * recebeu_treinamento_bemestar
)

# Normaliza para ficar entre 0 e 1
risco_burnout_prob = 1 / (1 + np.exp(-risco_burnout_prob))
# Gera 0 ou 1 com base na probabilidade
risco_burnout = (np.random.rand(n) < risco_burnout_prob).astype(int)

# Monta o DataFrame
df = pd.DataFrame({
    "id_funcionario": ids,
    "cargo": cargos,
    "horas_trabalhadas_semanais": horas_trabalhadas,
    "humor_diario": humor_diario,
    "trabalho_remoto": trabalho_remoto,
    "idade": idade,
    "tempo_empresa_anos": tempo_empresa_anos,
    "recebeu_treinamento_bemestar": recebeu_treinamento_bemestar,
    "pontuacao_engajamento": pontuacao_engajamento,
    "faltas_3_meses": faltas_3_meses,
    "risco_burnout": risco_burnout
})

# Salva o CSV
df.to_csv("dados/dados_bem_estar.csv", index=False, encoding="utf-8-sig")
print("Arquivo dados_bem_estar.csv gerado na pasta dados/")
