import requests
import base64
import pandas as pd
import json


filtro = {
    "language": "pt-br",
    "pageNumber": 1,
    "pageSize": 100,
    "index": "IBOV",
    "segment": "1",
}


ibov_api = "https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/{filtro}"


filtro_encoded = base64.b64encode(str(filtro).encode()).decode()

response = requests.get(ibov_api.format(filtro=filtro_encoded))

data = response.json()

df = pd.DataFrame(data.get("results", []))

df.to_parquet("ibov.parquet", index=False)


