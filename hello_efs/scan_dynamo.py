import json
import boto3

def lambda_handler(event, context):
    try:
        client = boto3.client('dynamodb')
        data = client.scan(
            TableName='products'
            )
        response = {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
        return response

    except Exception as e:
        print("Exception: ", e)


  