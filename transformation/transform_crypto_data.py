import boto3
import json
from datetime import datetime
import os

# Configurações
BUCKET = "crypto-pipeline-dados-mathvieger"
RAW_PREFIX = "raw"
TRUSTED_PREFIX = "trusted"

s3 = boto3.client("s3")

def listar_arquivos_raw():
    # Lista os arquivos do prefixo RAW
    resposta = s3.list_objects_v2(Bucket=BUCKET, Prefix=RAW_PREFIX)
    arquivos = [item["Key"] for item in resposta.get("Contents", []) if item["Key"].endswith(".json")]
    return arquivos

def transformar_dado(conteudo, cripto_nome):
    # Adiciona metadata ao dado
    preco = conteudo.get(cripto_nome, {}).get("usd")
    return {
        "cripto": cripto_nome,
        "preco_usd": preco,
        "timestamp_processamento": datetime.utcnow().isoformat()
    }

def processar_arquivo(chave):
    print(f"Processando: {chave}")

    # Extrair nome da cripto (bitcoin_2025-07-10.json)
    nome_arquivo = os.path.basename(chave)
    nome_cripto = nome_arquivo.split("_")[0]

    obj = s3.get_object(Bucket=BUCKET, Key=chave)
    conteudo = json.loads(obj["Body"].read())

    dado_transformado = transformar_dado(conteudo, nome_cripto)

    # Mesma partição de data
    pasta_destino = chave.replace(RAW_PREFIX, TRUSTED_PREFIX).replace(nome_arquivo, "")
    novo_nome = nome_arquivo.replace(".json", "_trusted.json")

    s3.put_object(
        Bucket=BUCKET,
        Key=f"{pasta_destino}{novo_nome}",
        Body=json.dumps(dado_transformado),
        ContentType="application/json"
    )

if __name__ == "__main__":
    arquivos = listar_arquivos_raw()
    for arquivo in arquivos:
        processar_arquivo(arquivo)
