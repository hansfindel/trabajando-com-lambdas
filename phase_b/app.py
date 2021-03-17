import json
def lambda_handler(event : dict, context):
    print("B")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "B",
            "prev" : event["body"]
            # "location": ip.text.replace("\n", "")
        }),
    }