# AWS Crypto Pipeline Analysis 📊 (em construção)

Este projeto é um pipeline de dados end-to-end para coletar, armazenar, transformar e consultar cotações de criptomoedas usando ferramentas da AWS.
Os dados serão coletados da Coingecko que disponibiliza um API gratuito com atualização near real-time.

## 🔧 Tecnologias usadas
- AWS S3
- AWS Glue
- AWS Lambda
- AWS CloudWatch
- CoinGecko API
- Python

## 📐 Arquitetura (Resumo)
1. Ingestão dos dados via API CoinGecko
2. Armazenamento no S3 (camada raw)
3. Transformação e limpeza dos dados (camada trusted)
4. Consulta com Athena
5. Automatização com Lambda
6. Monitoramento com CloudWatch
7. Versionamento com Github.

## 📁 Estrutura do Projeto
- `ingestion/`: Scripts de ingestão da API CoinGecko: sempre que o API disponibiliza um novo arquivo em sua plataforma, um script em Lambda faz a leitura deste novo material e lança no S3 do projeto, deixando-o sempre atualizado. Na pasta, encontra-se o .zip dessa estrutura.
- `transformation/`: Scripts de tratamento e limpeza: foram criados dois scripts em Lambda para automatizar o tratamento e limpeza dos dados ingeridos para valores trabalháveis. O script batch faz a leitura em lote dos arquivos que forem chegando - um máximo de 1.000 por lote - para uma leitura mais lenta. Além disso, também foi criado um script em speed para que, assim que a raw/ for atualizada, faça-se a leitura do arquivo e atualize a pasta trusted/. Ambos estão zipados nesta pasta.
- `infrastructure/`: Infraestrutura como código (futuramente)
- `docs/`: Documentação extra (futuramente)
- `tests/`: Testes automatizados (futuramente)

## 📊 Fonte dos Dados
- [CoinGecko API](https://www.coingecko.com/en/api)

## 🛡️ Segurança
- Uso de AWS IAM com políticas mínimas
- Dados sensíveis fora do controle de versão

---
