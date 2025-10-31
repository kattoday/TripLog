import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TripLog')
comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    trip_id = str(uuid.uuid4())
    trip_name = body.get('tripName')
    location = body.get('location')
    date = body.get('date')
    notes = body.get('notes')

    sentiment_response = comprehend.detect_sentiment(Text=notes, LanguageCode='en')
    entities_response = comprehend.detect_entities(Text=notes, LanguageCode='en')

    sentiment = sentiment_response['Sentiment']
    entities = [e['Text'] for e in entities_response['Entities']]

    item = {
        'tripId': trip_id,
        'tripName': trip_name,
        'location': location,
        'date': date,
        'notes': notes,
        'sentiment': sentiment,
        'entities': entities
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'headers': { 'Access-Control-Allow-Origin': '*' },
        'body': json.dumps({
            'message': 'Trip saved',
            'tripId': trip_id,
            'sentiment': sentiment,
            'entities': entities
        })
    }
