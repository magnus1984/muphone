import json
import phonenumbers

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
        phone_number = json.loads(event['body'])['phone']
    except:
        error = {'message':'POST request must contain phone'}
        return response(400, error)


    try:
        number = phonenumbers.parse(phone_number, 'US')
    except:
        return response(400, {'message':'the provided string does not appear to be a phone number'})

    if not phonenumbers.is_valid_number(number):
        return response(400, {'message':'the provided phone number is invalid'})


    formated_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)


    return response(200, {'number':formated_number})
