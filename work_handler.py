import json

def default_handler(event, context):
    # print('event', event)
    # print('event type', type(event)) : dict

    # lambda handlerは基本dict型だが、中身がstrの可能性あり。
    # print('event[body] type', type(event["body"])) : str
    
    # そういう時はstrをdict展開
    # ev = json.loads(event["body"])
    
    # そうすれば読める.
    # sakename = ev["queryResult"]["parameters"]["sakename"]
    # query = ev["queryResult"]["intent"]["displayName"]
    
    # print('sakename', sakename)
    # print('query' , query)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            "fulfillment_text": "show text from aws lambda",
            "fulfillment_messages":[{
                "text" : {
                    "text" : [
                        "Hello from Lambda!",
                    ]
                }
            }]
        })
    }
