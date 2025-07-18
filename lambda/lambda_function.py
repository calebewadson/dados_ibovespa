import json
import boto3

def lambda_handler(event, context):
    glue_client = boto3.client('glue')

    glue_job_name = 'glue-fiap-ibovespa' 
    
    print(f"Acionando o job Glue: {glue_job_name}")

    try:
        response = glue_client.start_job_run(JobName=glue_job_name)
        print(f"Job Glue acionado com sucesso. RunId: {response['JobRunId']}")
        return {
            'statusCode': 200,
            'body': json.dumps(f'Glue job {glue_job_name} started successfully with RunId: {response["JobRunId"]}')
        }
    except Exception as e:
        print(f"Erro ao acionar o job Glue: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error starting Glue job {glue_job_name}: {str(e)}')
        }
    