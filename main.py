import sys
import os
from datetime import datetime
from src.data_ingestion.b3_scraper import (
    get_ibov_portfolio,
    save_dataframe_as_parquet_daily,
)
from src.data_storage.s3_uploader import upload_file_to_s3
from src.config import (
    S3_BUCKET_NAME,
    LOCAL_DATA_BASE_PATH,
    LOCAL_FILE_PREFIX,
    LOCAL_FILE_NAME_FORMAT
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


def run_daily_process():
    print("--- Iniciando processo diário de dados do IBOV ---")

    ibov_df = get_ibov_portfolio()
    if ibov_df.empty:
        print("Não foi possível obter dados do IBOV. Encerrando o processo.")
        return

    print("Salvando dados localmente em formato Parquet...")

    local_file_path = save_dataframe_as_parquet_daily(ibov_df)

    if not local_file_path:
        print("Falha ao salvar o arquivo parquet localmente.")
        return

    data_obj = datetime.now()
    data_str = data_obj.strftime("%Y%m%d")

    s3_object_key = LOCAL_FILE_NAME_FORMAT.format(
        date=data_str, prefix=LOCAL_FILE_PREFIX
    )

    print(
        f"Fazendo upload de '{local_file_path}' para s3://{S3_BUCKET_NAME}/{s3_object_key}..."
    )
    success = upload_file_to_s3(local_file_path, s3_object_key)

    if success:
        print("Processo diário concluído com sucesso!")
    else:
        print("Processo diário concluído com erros de upload.")


if __name__ == "__main__":
    run_daily_process()
