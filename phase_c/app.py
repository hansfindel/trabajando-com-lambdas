import json
def lambda_handler(event : dict, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "C",
            "prev" : event["body"]
            # "location": ip.text.replace("\n", "")
        }),
    }