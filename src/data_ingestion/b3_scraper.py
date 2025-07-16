import requests
import json
import base64
import pandas as pd
from datetime import datetime, timedelta
import os
from src.config import (
    B3_IBOV_API_BASE_URL,
    B3_API_DEFAULT_FILTERS,
    LOCAL_DATA_BASE_PATH,
    LOCAL_FILE_PREFIX,
    LOCAL_FILE_NAME_FORMAT,
)


def get_ibov_portfolio(filters=None):
    if filters is None:
        filters = B3_API_DEFAULT_FILTERS.copy()

    filtro_encoded = base64.b64encode(str(filters).encode()).decode()
    ibov_api_url = f"{B3_IBOV_API_BASE_URL}{filtro_encoded}"

    try:
        response = requests.get(ibov_api_url)
        response.raise_for_status()
        data_json = response.json()
        df = pd.DataFrame(data_json.get("results", []))
        if "theoricalQty" in df.columns:
            df["theoricalQty"] = df["theoricalQty"].astype(str).str.replace(".", "", regex=False)
        if "part" in df.columns:
            df["part"] = df["part"].astype(str).str.replace(",", ".", regex=False)
        current_date = datetime.now() - timedelta(days=1)
        current_date = current_date.strftime("%Y-%m-%d")
        df["data_pregao"] = current_date
        return df

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da B3: {e}")
        return pd.DataFrame()


def save_dataframe_as_parquet_daily(df):
    if df.empty:
        print("DataFrame vazio, não há dados para salvar.")
        return

    data_obj = datetime.now()
    data_str = data_obj.strftime("%Y%m%d")

    file_name = LOCAL_FILE_NAME_FORMAT.format(date=data_str, prefix=LOCAL_FILE_PREFIX)

    file_path = os.path.join(LOCAL_DATA_BASE_PATH, file_name)

    os.makedirs(LOCAL_DATA_BASE_PATH, exist_ok=True)

    try:
        df.to_parquet(file_path, index=False)
        print(f"Dados do IBOV salvos em {file_path} com sucesso!")
        return file_path
    except Exception as e:
        print(f"Erro ao salvar arquivo Parquet: {e}")
        return pd.DataFrame()
