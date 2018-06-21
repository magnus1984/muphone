import json
import phonenumbers

import boto3
import os

def get_dynamodb_phone_table():

    if os.getenv('AWS_SAM_LOCAL'):
        table = boto3.resource('dynamodb', endpoint_url='http://dynamodb:8000').Table('phone')
    else:
        table = boto3.resource('dynamodb').Table(os.get('DYNAMODB_PHONE_TABLE_NAME'))

    return table

def response(status, payload):
    """ Creates a response object as requested by AWS lambda

    Arguments:
        status integer -- HTTP status code to return
        payload dict -- return dict to be serialized and included in the body

    Returns:
        dict -- {'statusCode': int, 'body':string}
    """

    return {
        'statusCode': status,
        'body': json.dumps(payload)
        }

def new_phone_number(event, context):
    """ Creates a new phone number to verify

    Arguments:
        event LambdaEvent -- Lambda Event received from Invoke API
        context LambdaContext -- Lambda Context runtime methods and attributes

    Returns:
        dict -- {'statusCode': int, 'body': dict}
    """

    phone_number = None
    try:
        phone_number = json.loads(event['body'])['number']
    except:
        error = {'message':'POST request must contain a number field'}
        return response(400, error)


    try:
        number = phonenumbers.parse(phone_number, 'US')
    except:
        return response(400, {'message':'the provided string does not appear to be a phone number'})

    if not phonenumbers.is_valid_number(number):
        return response(400, {'message':'the provided phone number is invalid'})

    formated_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
    init_state = 'NEW'
    validation_code = validation.code()

    item = {'number':formated_number, 'state': init_state, 'validation_code':validation_code}
    table = get_dynamodb_phone_table()

    table.put_item(Item=item)

    return response(200, item)

def phone_number(event, context):

    number = None
    try:
        number = event['queryStringParameters']['number']
    except:
        error = {'message':'request must include the number query string parameter'}
        return response(400, error)

    table = get_dynamodb_phone_table()
    try:
        item = table.get_item(Key={'number':number})['Item']
    except:
        return response(200, None)

    return response(200, item)

def validate_number(event, context):

    number = None
    validation



