# **WellWork AI – Plataforma Inteligente de Bem-Estar no Trabalho**

O **WellWork AI** é uma plataforma que utiliza dados simulados e técnicas de Inteligência Artificial para **monitorar bem-estar, engajamento e risco de burnout** em ambientes corporativos.
O sistema integra diversas tecnologias — Python, R, Machine Learning, Redes Neurais, Banco de Dados, API e conceitos de Cloud e Cybersecurity — criando uma solução completa, modular e aplicável ao cenário de RH e saúde mental.

---

## **📌 Objetivo do Projeto**

Criar uma solução integrada capaz de:

* Coletar e organizar dados sobre colaboradores (horas trabalhadas, humor, engajamento etc.)
* Realizar análise exploratória e visualização estatística
* Treinar modelos de Machine Learning e Redes Neurais para prever **risco de burnout**
* Persistir e consultar os dados via banco relacional
* Disponibilizar o modelo por meio de uma **API FastAPI**
* Possibilitar uso futuro em aplicações em nuvem e dashboards corporativos

---

## **📂 Estrutura do Repositório**

```
wellwork_ai/
  dados/
    dados_bem_estar.csv
    modelo_rf.pkl
    modelo_rn.h5
    preprocessador_rn.pkl
    wellwork.db
  python/
    gerar_dados.py
    ml_modelo_classico.py
    rn_modelo_neural.py
    banco_dados.py
    api_fastapi.py
  r/
    analise_exploratoria.R
  doc/
    relatorio_global_solution.pdf
    arquitetura.png
```

---

# **🧩 Componentes do Projeto**

Abaixo estão os módulos que compõem a solução, conforme desenvolvido na GS2:

---

## **1️⃣ Geração de Dados Simulados (Python)**

Arquivo: `python/gerar_dados.py`

Simula um conjunto de **500 funcionários**, gerando variáveis como:

* Cargo
* Horas trabalhadas semanais
* Humor diário
* Idade
* Engajamento
* Trabalho remoto
* Treinamento de bem-estar
* Faltas
* **Risco de burnout (variável alvo)**

O resultado é salvo em:
`dados/dados_bem_estar.csv`

---

## **2️⃣ Análise Exploratória em R**

Arquivo: `r/analise_exploratoria.R`

Executa:

* Estatísticas descritivas
* Conversão de variáveis para fatores
* Histogramas
* Boxplots
* Médias agrupadas

Principais insights apresentados no relatório:
Funcionários com maior risco de burnout tendem a:

* Trabalhar mais horas
* Ter menor humor médio
* Apresentar engajamento reduzido

---

## **3️⃣ Modelo de Machine Learning – Random Forest**

Arquivo: `python/ml_modelo_classico.py`

Etapas:

* Pré-processamento (One-Hot Encoder + ColumnTransformer)
* Treino/teste com **Random Forest**
* Relatório de classificação
* Matriz de confusão
* Salvamento do modelo em `modelo_rf.pkl`

Esse modelo é usado posteriormente pela API FastAPI.

---

## **4️⃣ Modelo de Rede Neural – Keras/TensorFlow**

Arquivo: `python/rn_modelo_neural.py`

Arquitetura:

* Camada densa (32 neurônios, ReLU)
* Camada densa (16 neurônios, ReLU)
* Camada final (1 neurônio, Sigmoid)
* Treino por 30 epochs

Saídas salvas:

* `modelo_rn.h5`
* `preprocessador_rn.pkl`

Modelo utilizado para comparação entre ML tradicional e Deep Learning.

---

## **5️⃣ Banco de Dados – SQLite + CRUD em Python**

Arquivo: `python/banco_dados.py`

Funções:

* Criação do banco `wellwork.db`
* Tabelas:

  * `funcionarios`
  * `bem_estar_diario`
* Inserção dos dados simulados no banco
* Estrutura pensada para expansão futura (ex.: históricos diários)

---

## **6️⃣ API FastAPI – Previsão de Risco de Burnout**

Arquivo: `python/api_fastapi.py`

Rotas principais:

```
GET /
POST /prever_risco
```

A API recebe dados de um funcionário e retorna:

```json
{
  "risco_burnout": 1,
  "probabilidade_risco": 0.82
}
```

Rodar localmente:

```
uvicorn api_fastapi:app --reload
```

Documentação automática (Swagger):
`http://127.0.0.1:8000/docs`

---

# **📡 Integração com Cloud Computing**

A solução pode ser facilmente implantada em:

* **Render**
* **Railway**
* **Azure App Service**
* **AWS EC2 / Lambda**
* **Google Cloud Run**

Fluxo sugerido:

1. API FastAPI deployada na nuvem
2. Banco substituído por PostgreSQL gerenciado
3. Armazenamento dos modelos em blob storage
4. Dashboard ou app acessando a API

---

# **🔐 Cybersecurity e LGPD**

O projeto aborda:

* Proteção de dados sensíveis (saúde/engajamento)
* Necessidade de autenticação (ex.: Token ou JWT)
* Comunicação segura (HTTPS)
* Princípios da LGPD:

  * Minimização de dados
  * Finalidade clara
  * Transparência
  * Armazenamento seguro

Um header de autenticação pode ser facilmente adicionado à API, caso necessário.

---

# **🌱 Formação Social – Impacto Social e Ética**

O WellWork AI:

* Auxilia empresas a prevenir burnout e promover qualidade de vida
* Incentiva pausas, equilíbrio e práticas de bem-estar
* Identifica padrões de risco sem discriminar perfis
* Evita uso punitivo dos dados (ética + LGPD)
* Complementa — e não substitui — o suporte humano (líderes, psicólogos, RH)

---

# **🚀 Como Executar o Projeto**

### **1. Criar dados**

```
cd python
python gerar_dados.py
```

### **2. Analisar no R**

Abrir `r/analise_exploratoria.R` no RStudio e executar.

### **3. Treinar modelo ML**

```
python ml_modelo_classico.py
```

### **4. Treinar rede neural**

```
python rn_modelo_neural.py
```

### **5. Gerar banco de dados**

```
python banco_dados.py
```

### **6. Rodar API**

```
uvicorn api_fastapi:app --reload
```

---

# **🖼️ Arquitetura da Solução**

*(inserir o arquivo arquitetura.png na pasta doc/)*

---

# **📹 Link do vídeo**

