import json
import boto3

def lambda_handler(event, context):
    print("Event:", event)
    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = record["s3"]["object"]["key"]

    return {"status": "done", "file": key}
