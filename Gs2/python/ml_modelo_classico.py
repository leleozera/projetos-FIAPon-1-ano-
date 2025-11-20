import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

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

# 4. Pré-processamento
preprocessador = ColumnTransformer(
    transformers=[
        ("num", "passthrough", colunas_numericas),
        ("cat", OneHotEncoder(handle_unknown="ignore"), colunas_categoricas)
    ]
)

# 5. Modelo de ML
modelo_rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

# 6. Pipeline final
pipeline = Pipeline(steps=[
    ("preprocessamento", preprocessador),
    ("modelo", modelo_rf)
])

# 7. Treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline.fit(X_treino, y_treino)

y_pred = pipeline.predict(X_teste)

print("Relatório de classificação (Random Forest):")
print(classification_report(y_teste, y_pred))
print("Matriz de confusão:")
print(confusion_matrix(y_teste, y_pred))

# 8. Salvar o modelo treinado
import joblib
joblib.dump(pipeline, "dados/modelo_rf.pkl")
print("Modelo Random Forest salvo em dados/modelo_rf.pkl")
