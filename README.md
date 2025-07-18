# Pipeline de Dados Big Data Serverless para Análise do Ibovespa

Este projeto, desenvolvido como parte da segunda etapa da pós-graduação em Engenharia de Machine Learning, implementa uma pipeline de Big Data serverless para coletar, processar e analisar dados históricos do Ibovespa.

## Visão Geral da Arquitetura

A arquitetura do projeto é totalmente serverless e construída na AWS, conforme ilustrado no diagrama abaixo (consulte a imagem `arquitetura de big data.jpng` para uma representação visual):
![Arquitetura do Projeto](./img/arquitetura%20de%20big%20data.png "Big Data Architecture")

* **Coleta de Dados:** Um script Python customizado (Scraper Bovespa Sob Demanda) é responsável por extrair dados do portfólio do Ibovespa diretamente do site da B3.
* **Armazenamento Bruto:** Os dados brutos coletados são armazenados em um bucket S3 (`Raw Bucket Bovespa`) para persistência e como ponto de partida para o processamento ETL.
* **Trigger de Processamento:** Uma função AWS Lambda (`Lambda Trigger AWS Glue`) é configurada para ser acionada em resposta à chegada de novos dados no bucket S3 bruto, orquestrando o início do processo ETL.
* **Processamento ETL:** O AWS Glue (`Glue ETL Bovespa`) é utilizado para realizar transformações e limpezas nos dados brutos, preparando-os para análise.
* **Armazenamento Refinado:** Os dados processados e refinados são armazenados em um segundo bucket S3 (`Amazon S3 Refined Bovespa`), otimizados para consultas e análises.
* **Análise e Dashboards:** O Amazon Athena é empregado para consultar os dados refinados, permitindo a criação de dashboards e a execução de análises complexas.
* **Consumo pelo Cliente Final:** O objetivo final é fornecer acesso aos dados e insights para o cliente final, facilitando a tomada de decisões.

## Estrutura do Projeto

O repositório do projeto contém o código-fonte para as seguintes componentes:

* **`scraper_bovespa/`**: Contém o script Python para a raspagem de dados do site da B3.
* **`lambda_function/`**: Código da função AWS Lambda que atua como trigger.


## Como Executar

### Pré-requisitos

* Conta AWS configurada.
* Credenciais AWS configuradas localmente.
* Python 3.10 instalado.
* Bibliotecas Python necessárias (especificadas em `requirements.txt`).

### Passos para Implantação e Execução

1.  **Configurar Buckets S3:** Crie as pastas no seu bucket S3 (`raw` e `refined`) em sua conta AWS.
2.  **Configurar AWS Glue:**
    * Desenvolva e configure um Job Glue que leia do `Raw`, execute as transformações e grave no `Refined`.
3.  **Configurar AWS Lambda:**
    * Crie uma função Lambda.
    * Configure o trigger da Lambda para ser o evento `ObjectCreated` no `Raw `.
    * O código da função Lambda deve invocar o Job Glue configurado.
4.  **Executar o Scraper:**
    * Navegue até o diretório `IBOVESPA`.
    * Instale as dependências: `pip install -r requirements.txt`
    * Execute o script Python: `python main.py` (ou o nome do seu arquivo principal do scraper).
    * Este script fará o upload dos dados para o `Raw`, acionando a pipeline.
5.  **Analisar Dados com Athena:**
    * No console do Amazon Athena, crie uma tabela que aponte para o `Refined`.
    * Comece a executar suas consultas SQL para analisar os dados.

## Tecnologias Utilizadas

* **AWS S3:** Armazenamento de objetos escalável.
* **AWS Lambda:** Computação serverless para acionar a pipeline.
* **AWS Glue:** Serviço ETL serverless para processamento de dados.
* **Amazon Athena:** Serviço de consulta interativa para dados em S3.
* **Python:** Linguagem de programação para o scraper e scripts ETL.

