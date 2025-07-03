B3_IBOV_API_BASE_URL = (
    'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/'
)

B3_API_DEFAULT_FILTERS = {
    'language': 'pt-br',
    'pageNumber': 1,
    'pageSize': 100,
    'index': 'IBOV',
    'segment': '1',
}

S3_BUCKET_NAME = 'ibovespa-fiap'

LOCAL_DATA_BASE_PATH = 'data'
LOCAL_FILE_PREFIX = 'ibov_portfolio'
LOCAL_FILE_NAME_FORMAT = '{date}.{prefix}.parquet'
