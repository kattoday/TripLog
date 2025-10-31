import json
import boto3
import os
from boto3.dynamodb.conditions import Attr

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Safely extract and normalize query parameter
        query_params = event.get('queryStringParameters', {})
        sentiment = query_params.get('sentiment', '').upper()

        # Build filter expression if sentiment is provided
        if sentiment:
            response = table.scan(
                FilterExpression=Attr('sentiment').eq(sentiment)
            )
        else:
            response = table.scan()

        items = response.get('Items', [])

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,GET'
            },
            'body': json.dumps(items)
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
    'statusCode': 500,
    'headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST'
    },
    'body': json.dumps({'message': 'Internal Server Error'})
}
