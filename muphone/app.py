import json

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

    print(event)
    return response(200, {'message':'all good'}



