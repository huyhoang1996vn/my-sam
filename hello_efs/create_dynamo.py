import json
from pathlib import Path

# You can reference EFS files by including your local mount path, and then
# treat them like any other file. Local invokes may not work with this, however,
# as the file/folders may not be present in the container.
# FILE = Path("/mnt/lambda/file")
import boto3
import uuid
def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('products')
        data_dict = json.loads(event.get("body"))
        data_dict['id'] = uuid.uuid4().hex

        data_return = table.put_item(
            Item=data_dict
            )
        response = {
            'statusCode': 200,
            'body': json.dumps(data_return),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
        return response

    except Exception as e:
        print("Exception: ", e)


  