# dashboard/app.py
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# --- Configuração ---
SQLITE_DB = "sensor_data.db"
GAS_THRESHOLD = 800  # O mesmo threshold usado no ml_pipeline.py
st.set_page_config(layout="wide")

# Função para carregar dados do SQLite
@st.cache_data
def load_data(db_path):
    conn = sqlite3.connect(db_path)
    # Seleciona as leituras e o status de alerta (0=OK, 1=ALERTA)
    query = """
    SELECT
        strftime('%Y-%m-%d %H:%M:%S', timestamp) as timestamp_str,
        temperature,
        humidity,
        gas_value
    FROM reading
    ORDER BY timestamp DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Converte timestamp para datetime
    df['timestamp'] = pd.to_datetime(df['timestamp_str'])
    
    # Cria a coluna de status_alerta baseada no threshold para visualização
    df['status_alerta'] = (df['gas_value'] > GAS_THRESHOLD).astype(int)
    
    return df

# --- Aplicação Streamlit ---
st.title("🏭 Dashboard Industrial IoT - Hermes Reply Challenge")
st.markdown("Monitoramento e Análise Preditiva de Sensores Industriais")

try:
    data = load_data(SQLITE_DB)
    
    # --- Alerta Mínimo e KPI de Alertas ---
    latest_reading = data.iloc[0]
    
    # Alerta Mínimo (Temperatura > X OU Gás > Y)
    is_gas_alert = latest_reading['gas_value'] > GAS_THRESHOLD
    
    if is_gas_alert:
        st.error(f"🚨 ALERTA ATIVADO: Vazamento de Gás! Valor mais recente: {latest_reading['gas_value']} PPM")
    else:
        st.success("✅ Sistema Operacional: Nível de Gás e Temperatura dentro da normalidade.")
        
    st.markdown("---")
    
    # Métricas e KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    # KPI 1: Temperatura Média
    col1.metric(label="Temperatura Média (°C)", value=f"{data['temperature'].mean():.2f}")
    
    # KPI 2: Umidade Média
    col2.metric(label="Umidade Média (%)", value=f"{data['humidity'].mean():.2f}")
    
    # KPI 3: Número de Alertas (Gás > 800)
    total_alerts = data['status_alerta'].sum()
    col3.metric(label="Total de Alertas de Gás", value=total_alerts)

    # KPI 4: Último Gás Registrado
    col4.metric(label="Último Gás (PPM)", value=f"{latest_reading['gas_value']}")

    st.markdown("---")

    # --- Gráfico da Série Temporal ---
    st.header("Série Temporal de Gás e Temperatura")
    
    # Gráfico do Gás (o mais crítico para o alerta)
    st.subheader("Nível de Gás (PPM)")
    st.line_chart(data, x='timestamp', y='gas_value', color="#ff0000")
    
    # Gráfico da Temperatura
    st.subheader("Temperatura (°C)")
    st.line_chart(data, x='timestamp', y='temperature')

except FileNotFoundError:
    st.error(f"Erro: O banco de dados '{SQLITE_DB}' não foi encontrado. Execute o 'ml_pipeline.py' primeiro.")
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar os dados: {e}")
    
st.caption("Base de dados carregada do arquivo sensor_data.db. O status do ML (acurácia) deve ser reportado no README ou em uma seção separada.")