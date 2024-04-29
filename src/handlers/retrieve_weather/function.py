def handler(event, context): #test lambda handler
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
