import requests
import base64
import json

ibov_api = "https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/{filtro}"

filtro = {
    "language": "pt-br",
    "pageNumber": 1,
    "pageSize": 100,
    "index": "IBOV",
    "segment": "1",
}

filtro_encoded = base64.b64encode(str(filtro).encode()).decode()

response = requests.get(ibov_api.format(filtro=filtro_encoded))

with open("ibov.json", "w") as file:
    json.dump(response.json(), file, indent=4, ensure_ascii=False)
