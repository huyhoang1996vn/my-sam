import json
import io 
import boto3
import pathlib

def lambda_handler(event, context):
    print("==== path ", pathlib.Path(__file__).parent.resolve())
    file_binary = open("/var/task/media/dog-2.jpg", "rb").read()
    file_as_binary = io.BytesIO(file_binary)
    s3 = boto3.client('s3')
    resp = s3.upload_fileobj(file_as_binary, "test-media-incloud-2", "dog4.png")
    # with open("/home/steve/Documents/my-sam/media/dog.png", "rb") as f:
    # s3.upload_file("dog.png","test-media-incloud" , "dog.png")
    print("==== resp ", resp)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success",
        }),
    }