import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# 1. Carregar dados
df = pd.read_csv("dados/dados_bem_estar.csv")

# 2. Separar features e alvo
X = df.drop(columns=["risco_burnout", "id_funcionario"])
y = df["risco_burnout"]

# 3. Definir colunas numéricas e categóricas
colunas_numericas = [
    "horas_trabalhadas_semanais",
    "humor_diario",
    "idade",
    "tempo_empresa_anos",
    "pontuacao_engajamento",
    "faltas_3_meses",
    "recebeu_treinamento_bemestar",
    "trabalho_remoto"
]
colunas_categoricas = ["cargo"]

# 4. Pré-processador: padronizar numéricas + one-hot em categóricas
preprocessador = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), colunas_numericas),
        ("cat", OneHotEncoder(handle_unknown="ignore"), colunas_categoricas),
    ]
)

# 5. Definir rede neural MLP
mlp = MLPClassifier(
    hidden_layer_sizes=(32, 16),  # duas camadas ocultas: 32 e 16 neurônios
    activation="relu",
    max_iter=300,
    random_state=42
)

# 6. Pipeline completo
pipeline = Pipeline(steps=[
    ("preprocessamento", preprocessador),
    ("modelo", mlp)
])

# 7. Treino/teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline.fit(X_treino, y_treino)

y_pred = pipeline.predict(X_teste)

print("Relatório de classificação (Rede Neural MLP):")
print(classification_report(y_teste, y_pred))
print("Matriz de confusão:")
print(confusion_matrix(y_teste, y_pred))

# 8. Salvar modelo
joblib.dump(pipeline, "dados/modelo_rn.pkl")
print("Rede neural MLP salva em dados/modelo_rn.pkl")
