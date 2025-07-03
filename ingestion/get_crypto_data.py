import requests
import boto3
import json
from datetime import datetime
import os

# Configurações
CRYPTO_ID = 'bitcoin'
CURRENCY = 'usd'
BUCKET_NAME = 'krypto-koin-case'
RAW_PATH = 'raw'

# Conecta ao S3
s3 = boto3.client('s3')

# Pega a data de hoje
today = datetime.utcnow().strftime('%Y-%m-%d')

def get_crypto_data(crypto_id, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_to_s3(data, crypto_id):
    filename = f"{crypto_id}_{today}.json"
    s3_key = f"{RAW_PATH}/year={today[:4]}/month={today[5:7]}/day={today[8:10]}/{filename}"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=s3_key,
        Body=json.dumps(data),
        ContentType='application/json'
    )
    print(f"Arquivo enviado para o S3: s3://{BUCKET_NAME}/{s3_key}")

if __name__ == "__main__":
    try:
        print("Buscando dados da CoinGecko...")
        data = get_crypto_data(CRYPTO_ID, CURRENCY)
        save_to_s3(data, CRYPTO_ID)
    except Exception as e:
        print("Erro ao processar:", e)
