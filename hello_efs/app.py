import json
from pathlib import Path

# You can reference EFS files by including your local mount path, and then
# treat them like any other file. Local invokes may not work with this, however,
# as the file/folders may not be present in the container.
# FILE = Path("/mnt/lambda/file")
import boto3

def lambda_handler(event, context):
    try:
        client = boto3.client('dynamodb')
        data = client.get_item(
            TableName='products'
            )
    except Exception as e:
        print("========== ", e)

    response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
    return response