# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Enterprise Challenge – Fase 5  
## Hermes Reply – Modelagem de Banco de Dados e Machine Learning  

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Nunes Urbano 1</a>  
- <a href="https://www.linkedin.com/company/inova-fusca">Erick Souza Pereira 2</a>  

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>  
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>  

---

## 📜 Descrição

Este projeto foi desenvolvido como parte da **Fase 5 do Enterprise Challenge**, em parceria com a **Hermes Reply**.  
O objetivo é **modelar um banco de dados relacional** para armazenamento eficiente de dados de sensores industriais e aplicar **técnicas básicas de Machine Learning** para análise preditiva.  

A solução conecta as etapas anteriores do desafio (coleta de dados com ESP32 + Wokwi) à etapa atual, onde os dados são organizados em um banco relacional e usados como base para treinar um modelo de ML.  

---

## 🗄️ Banco de Dados

### DER (Diagrama Entidade-Relacionamento)  
O modelo relacional foi desenvolvido considerando boas práticas de normalização e integridade referencial.  
Entidades principais:  
- **device**: representa cada dispositivo IoT.  
- **sensor_type**: armazena tipos de sensores (temperatura, umidade, gás etc).  
- **sensor**: associa um dispositivo a um tipo de sensor específico.  
- **reading**: armazena os valores coletados em cada leitura.  
- **reading_status**: define categorias de status (ex: OK, ALERTA).  

📌 **DER Exportado:**  
<img src="assets/ER_diagram.png" width="70%">  

### Script SQL inicial
Arquivo: [`create_tables_sqlite.sql`](create_tables_sqlite.sql)  

Inclui:  
- Definição de **chaves primárias e estrangeiras**  
- Índices para otimizar consultas (`timestamp`, `status_id`)  
- Restrições de integridade  

---

## 🤖 Machine Learning

### Problema escolhido
O modelo busca **classificar risco de gás** a partir das leituras dos sensores.  
- `status` = **0 (OK)** ou **1 (ALERTA)**, definido com base no valor do sensor de gás.  

### Tecnologias
- **Python 3.11**  
- **Bibliotecas**: pandas, numpy, scikit-learn, matplotlib, joblib  

### Etapas realizadas
1. Extração dos dados simulados do banco SQLite.  
2. Pré-processamento no Pandas.  
3. Criação da variável alvo (`status`).  
4. Treinamento de um **Random Forest Classifier**.  
5. Avaliação com **accuracy** e **matriz de confusão**.  
6. Exportação de gráficos e salvamento do modelo.  

📊 **Resultados**:  
- Accuracy médio: ~0.90  
- Gráficos gerados:  
  - Matriz de confusão (`outputs/confusion_matrix.png`)  
  - Importância das features (`outputs/feature_importance.png`)  

---

## 📁 Estrutura de pastas

project/
│── assets/ # Logos e imagens (inclui ER exportado)
│── outputs/ # Gráficos e resultados do ML
│── models/ # Modelos treinados (joblib/pkl)
│── create_tables_sqlite.sql # Script SQL do banco
│── ER_diagram.mmd # Diagrama ER em Mermaid
│── sensor_data.db # Banco SQLite
│── simulated_readings.csv # Dados simulados
│── ml_pipeline.py # Pipeline de ML
│── README.md # Este documento

📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
