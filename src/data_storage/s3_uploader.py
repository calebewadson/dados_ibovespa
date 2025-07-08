import boto3
import os
from src.config import S3_BUCKET_NAME


def upload_file_to_s3(local_file_path, s3_object_key):
    s3 = boto3.client("s3")

    try:
        s3.upload_file(local_file_path, S3_BUCKET_NAME, s3_object_key)
        print(
            f'Arquivo "{local_file_path}" carregado com sucesso para s3://{S3_BUCKET_NAME}/{s3_object_key}'
        )
        return True
    except boto3.exceptions.S3UploadFailedError as e:
        print(f'Falha ao carregar "{local_file_path}" para o S3: {e}')
        return False
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return False
