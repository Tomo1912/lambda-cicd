import json

def lambda_handler(events, context):
    return{
        'statusCode': 200,
        'body': json.dumps('Hello from CICD Lambda')
    }