import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Descobrir a pasta raiz do projeto (D:\Gs2)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELO_PATH = os.path.join(BASE_DIR, "dados", "modelo_rf.pkl")

# Carrega o modelo treinado
modelo = joblib.load(MODELO_PATH)

app = FastAPI(
    title="WellWork AI - API de Bem-estar no Trabalho",
    description="API para prever risco de burnout com base em dados de funcionários.",
    version="1.0.0",
)

class FuncionarioInput(BaseModel):
    cargo: str
    horas_trabalhadas_semanais: float
    humor_diario: float
    trabalho_remoto: int
    idade: int
    tempo_empresa_anos: float
    recebeu_treinamento_bemestar: int
    pontuacao_engajamento: float
    faltas_3_meses: int

@app.get("/")
def raiz():
    return {"mensagem": "API WellWork AI no ar."}

@app.post("/prever_risco")
def prever_risco(dados: FuncionarioInput):
    try:
        df_entrada = pd.DataFrame([dados.dict()])
        prob = modelo.predict_proba(df_entrada)[0, 1]
        pred = modelo.predict(df_entrada)[0]

        return {
            "risco_burnout": int(pred),
            "probabilidade_risco": float(prob),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

