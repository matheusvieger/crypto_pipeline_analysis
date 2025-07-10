import json
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    crypto = "bitcoin"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    s3_bucket = "crypto-pipeline-dados-mathvieger"
    s3_prefix = "raw"

    now = datetime.utcnow()
    date_path = now.strftime("year=%Y/month=%m/day=%d")
    filename = f"{crypto}_{now.strftime('%Y-%m-%d')}.json"

    response = requests.get(url)
    data = response.json()

    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=s3_bucket,
        Key=f"{s3_prefix}/{date_path}/{filename}",
        Body=json.dumps(data),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Dados enviados com sucesso!")
    }
