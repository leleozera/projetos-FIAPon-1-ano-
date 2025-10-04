# ml_pipeline.py
import os
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import joblib

# --------- Configurações ----------
N_DEVICES = 3
READINGS_PER_DEVICE = 700   # ajuste para ter >=500 leituras por sensor
CSV_PATH = "simulated_readings.csv"
SQLITE_DB = "sensor_data.db"
MODEL_PATH = "models/rf_gas_alert.pkl"
OUTPUT_DIR = "outputs"
GAS_THRESHOLD = 800  # ajuste após calibração do MQ2
# ----------------------------------

os.makedirs("models", exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_simulated_data(n_devices=3, readings_per_device=700, start_ts=None, delta_seconds=5):
    np.random.seed(42)
    rows = []
    if start_ts is None:
        start_ts = datetime.now() - timedelta(seconds=readings_per_device*delta_seconds//2)
    for dev in range(1, n_devices+1):
        device_id = f"esp32_{dev}"
        ts = start_ts
        for i in range(readings_per_device):
            temp = float(np.round(np.random.normal(loc=25, scale=4), 2))
            hum = float(np.round(np.random.normal(loc=55, scale=10), 2))
            ldr = int(np.clip(np.random.normal(loc=1500, scale=600), 0, 4095))
            base_gas = np.random.normal(loc=200, scale=80)
            if np.random.rand() < 0.03:
                gas = int(np.clip(base_gas + np.random.normal(2000, 500), 0, 4095))
            else:
                gas = int(np.clip(base_gas, 0, 4095))
            accel_x = float(np.round(np.random.normal(loc=0.0, scale=0.8), 4))
            accel_y = float(np.round(np.random.normal(loc=0.0, scale=0.4), 4))
            accel_z = float(np.round(np.random.normal(loc=9.8, scale=0.6), 4))
            status = 1 if gas > GAS_THRESHOLD else 0
            raw = {"temp": temp, "hum": hum, "ldr": ldr, "gas": gas, "ax": accel_x}
            rows.append({
                "device_id": device_id,
                "timestamp": ts.isoformat(),
                "temperature": temp,
                "humidity": hum,
                "accel_x": accel_x,
                "accel_y": accel_y,
                "accel_z": accel_z,
                "ldr_value": ldr,
                "gas_value": gas,
                "raw_payload": str(raw),
                "status": status
            })
            ts = ts + timedelta(seconds=delta_seconds)
    return pd.DataFrame(rows)

def save_to_csv(df, path=CSV_PATH):
    df.to_csv(path, index=False)
    print(f"[OK] CSV salvo em: {path}")

def save_to_sqlite(df, db_path=SQLITE_DB, table_name="reading"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"[OK] Dados inseridos em SQLite: {db_path} -> tabela '{table_name}'")

def train_and_evaluate(df):
    features = ["temperature", "humidity", "accel_x", "accel_y", "accel_z", "ldr_value", "gas_value"]
    X = df[features].fillna(0)
    y = df["status"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("[RESULT] Accuracy:", acc)
    print("\n[REPORT]\n", classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(4,4))
    plt.imshow(cm, interpolation='nearest')
    plt.title("Confusion matrix")
    plt.colorbar()
    labels = ["OK","ALERT"]
    plt.xticks([0,1], labels)
    plt.yticks([0,1], labels)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i,j], ha="center", va="center",
                     color="white" if cm[i,j] > cm.max()/2 else "black")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    cm_path = os.path.join(OUTPUT_DIR, "confusion_matrix.png")
    plt.tight_layout()
    plt.savefig(cm_path)
    plt.close()
    print(f"[OK] Matriz de confusão salva em: {cm_path}")

    feat_imp = pd.Series(clf.feature_importances_, index=features).sort_values(ascending=False)
    plt.figure(figsize=(6,4))
    feat_imp.plot(kind='bar')
    plt.title("Feature importance")
    plt.tight_layout()
    fi_path = os.path.join(OUTPUT_DIR, "feature_importance.png")
    plt.savefig(fi_path)
    plt.close()
    print(f"[OK] Importância das features salva em: {fi_path}")

    joblib.dump(clf, MODEL_PATH)
    print(f"[OK] Modelo salvo em: {MODEL_PATH}")

if __name__ == "__main__":
    print("Gerando dados simulados...")
    df = generate_simulated_data(n_devices=N_DEVICES, readings_per_device=READINGS_PER_DEVICE)
    save_to_csv(df, CSV_PATH)
    save_to_sqlite(df, SQLITE_DB)
    print("Treinando modelo...")
    train_and_evaluate(df)
    print("Pipeline finalizado.")
