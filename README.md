# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto - Projeto Yolo

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Nunes Urbano 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Erick Souza Pereira 2</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>



## 🎯 Descrição do Projeto

1.Este projeto tem como objetivo desenvolver um modelo de **detecção de objetos** utilizando o algoritmo **YOLO (You Only Look Once)**.

O trabalho foi realizado a partir de um **conjunto de imagens de dois objetos** — um **mouse** e um **controle de videogame** — que foram **rotuladas manualmente** na plataforma **[MakeSense.ai](https://www.makesense.ai/)** para gerar os arquivos de anotação necessários ao treinamento do modelo.

Após o processo de rotulagem, os dados foram organizados em pastas de **treino**, **validação** e **teste**, permitindo o uso eficiente do modelo YOLO para:

* Treinar a rede neural com as imagens anotadas;
* Realizar testes de predição com novas imagens;
* Avaliar o desempenho do modelo por meio de métricas como **acurácia** e **precisão**.

Com isso, o projeto demonstra a aplicação prática da **Visão Computacional** e do **Aprendizado de Máquina** na identificação automática de objetos em imagens.

2.Classificação de Imagens com Redes Neurais Convolucionais (CNN). Este projeto tem como objetivo desenvolver e treinar uma Rede Neural Convolucional (CNN) capaz de classificar imagens em diferentes classes.

A CNN foi projetada e treinada utilizando um conjunto de imagens previamente rotuladas, aplicando técnicas de processamento de imagens, aumento de dados (data augmentation) e otimização de hiperparâmetros para alcançar uma boa taxa de acurácia no reconhecimento das classes.


## 📷 Link do vídeo

https://youtu.be/hFTIowB3OT8




## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.ipynb</b>: arquivo do colab, com todo o código utilizado


- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

Requisitos:

Acessar arquivo do colab, e rodar as seguintes intalações:

from google.colab import drive   
drive.mount('/content/drive')


!git clone https://github.com/ultralytics/yolov5.git


!pip install -r yolov5/requirements.txt


!pip install -q ultralytics 


!pip install -q tensorflow


!pip install -q opencv-python-headless


!pip install -q seaborn matplotlib scikit-learn pandas


!pip install numpy



## 🗃 Histórico de lançamentos

* 0.5.0 - 20/04/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - XX/XX/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

