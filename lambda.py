def handler(event, context):
            return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body':'Hello from Lambda!'
        ,
        "isBase64Encoded": False
    }