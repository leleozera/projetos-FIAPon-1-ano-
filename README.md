-----





````markdown


# FIAP - Faculdade de Informática e Administração Paulista





<p align="center">


<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>


</p>





<br>





# Enterprise Challenge – Fase 5: Pipeline de Dados Industrial 4.0





## Hermes Reply – Integração Fim-a-Fim: Sensor, ML e Dashboard





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





Este projeto é a **Entrega Final (Fase 5)** do Enterprise Challenge, consolidando a visão de arquitetura, simulação de coleta de dados e a modelagem em Machine Learning em um **MVP funcional**.





O objetivo é demonstrar um **pipeline de dados industrial 4.0** completo, onde leituras simuladas de sensores (ESP32) fluem de forma confiável para camadas analíticas e de decisão.





### **Integração e Vínculo com Fases Anteriores**





| Entrega | Foco | Decisão Técnica na Entrega 4 (MVP) |


| :--- | :--- | :--- |


| **Entrega 1** | Arquitetura Cloud/Edge | Implementação de uma **Arquitetura Edge/Monolítica** (Python/SQLite/Streamlit localmente) como *Proof of Concept* do fluxo completo. |


| **Entrega 2** | Simulação e Coleta | Utilização do **`simulated_readings.csv`** para replicar as leituras do circuito ESP32 (simulando múltiplos sensores, como Gás e Temperatura) e ingestão via carga *bulk*. |


| **Entrega 3** | Banco de Dados e ML | Utilização do **Modelo Relacional** de 5 tabelas (tabelas `DEVICE`, `READING`, etc.) no **SQLite** e operacionalização de um modelo de **Classificação (Random Forest)** para prever o estado de alerta. |





---





## 💻 Arquitetura e Fluxo Integrado





A arquitetura final ilustra o encadeamento dos blocos, desde a fonte de dados até a visualização e alertas.





-----





## 📁 Estrutura de pastas





A estrutura foi organizada para facilitar a reprodutibilidade e o acesso aos entregáveis de cada fase:





  - **`.github`**: Arquivos de configuração do GitHub.


  - **`assets`**: Imagens, logos e diagramas estáticos do projeto.


  - **`db`**: Contém o script `create_tables_sqlite.sql` e o banco de dados `sensor_data.db`.


  - **`ingest`**: Contém o arquivo `simulated_readings.csv` (simulação da coleta) e evidências iniciais.


  - **`ml`**: Contém o `ml_pipeline.py` (código de treino/inferência) e o modelo salvo.


  - **`outputs`**: Resultados visuais do ML (`confusion_matrix.png` e `feature_importance.png`).


  - **`dashboard`**: Contém o `app.py` da aplicação Streamlit (visualização e alertas).


  - **`README.md`**: Este documento.





-----





## 🔧 Como executar o código (Reprodutibilidade - Item 4.6)





Este guia detalha a ordem de execução para replicar o fluxo fim-a-fim.





### **Requisitos:**





  * Python 3.10 ou superior


  * Bibliotecas: `streamlit`, `pandas`, `scikit-learn`, `matplotlib`, `joblib`





<!-- end list -->





```bash


# Instalar dependências (o sqlite3 é nativo do Python)


pip install streamlit pandas scikit-learn matplotlib joblib


```





### **Ordem de Execução do Pipeline Completo:**





| Passo | Objetivo | Comando |


| :--- | :--- | :--- |


| **1. Criação do DB** | Criar o esquema de tabelas (Entrega 3). | `sqlite3 sensor_data.db < create_tables_sqlite.sql` |


| **2. Ingestão e ML** | Carregar dados, treinar o modelo e gerar as métricas. | `python ml_pipeline.py` |


| **3. Dashboard e Alerta** | Iniciar a interface de visualização. | `python -m streamlit run dashboard/app.py` |





-----





### **Alerta Mínimo **





O alerta mínimo é acionado no dashboard quando a leitura mais recente do `gas_value` excede o **threshold de 800 PPM**, conforme definido no `ml_pipeline.py`.





-----





## 🎥 Demonstração em Vídeo








**Link do YouTube: https://youtu.be/aAzQ2A8b1CQ


-----





## 🗃 Histórico de lançamentos





  * 0.5.0 - 20/04/2024 (Entrega Final - enterprise challenge)


  * 0.4.0 - XX/XX/2024 


  * 0.3.0 - XX/XX/2024


  * 0.2.0 - XX/XX/2024


  * 0.1.0 - XX/XX/2024





## 📋 Licença





\<img style="height:22px\!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"\>\<img style="height:22px\!important;margin-left:3px;vertical-align:text-bottom;width:22px;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"\>\<p xmlns:cc="http://creativecommons.org/ns\#" xmlns:dct="http://purl.org/dc/terms/"\>\<a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template"\>MODELO GIT FIAP\</a\> por \<a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br"\>Fiap\</a\> está licenciado sobre \<a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="\_blank" rel="license noopener noreferrer" style="display:inline-block;"\>Attribution 4.0 International\</a\>.\</p\>





```


```
