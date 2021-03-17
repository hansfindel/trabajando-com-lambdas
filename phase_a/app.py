import json
def lambda_handler(event : dict, context):
    print("A")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "A",
            "prev" : event
            # "location": ip.text.replace("\n", "")
        }),
    }