import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')  

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            outer = json.loads(record['body'])
            message = json.loads(outer['Message'])
            print("📦 Order received:", message)
            table.put_item(Item=message)

        except Exception as e:
            print("❌ ERROR:", str(e))
