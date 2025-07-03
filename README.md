# AWS Crypto Pipeline Analysis 📊 (em construção)

Este projeto é um pipeline de dados end-to-end para coletar, armazenar, transformar e consultar cotações de criptomoedas usando ferramentas da AWS.
Os dados serão coletados da Coingecko que disponibiliza um API gratuito com atualização near real-time.

## 🔧 Tecnologias usadas
- AWS S3
- AWS Glue
- AWS Athena
- AWS Step Functions
- AWS CloudWatch
- CoinGecko API
- Python

## 📐 Arquitetura (Resumo)
1. Ingestão dos dados via API CoinGecko
2. Armazenamento no S3 (camada raw)
3. Transformação e limpeza dos dados (camada trusted)
4. Consulta com Athena
5. Orquestração com Step Functions
6. Monitoramento com CloudWatch
7. Versionamento com Github.

## 📁 Estrutura do Projeto
- `ingestion/`: Scripts de ingestão da API CoinGecko
- `transformation/`: Scripts de tratamento e limpeza
- `infrastructure/`: Infraestrutura como código (futuramente)
- `docs/`: Documentação extra
- `tests/`: Testes automatizados

## 📊 Fonte dos Dados
- [CoinGecko API](https://www.coingecko.com/en/api)

## 🛡️ Segurança
- Uso de AWS IAM com políticas mínimas
- Dados sensíveis fora do controle de versão

---
