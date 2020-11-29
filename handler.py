
import ssl
import json
from websocket import create_connection

def send_word_to_channel(word, channel):
    ws = create_connection("wss://4etsjswwfl.execute-api.us-east-1.amazonaws.com/dev",sslopt={"cert_reqs": ssl.CERT_NONE})
    body = {"action": "sendMessage", "name": "Connor", "channelId": channel, "content": word}
    body = json.dumps(body)
    print(f"Sending {body}")
    ws.send(body)
    print("Sent")
    print("Receiving...")
    result =  ws.recv()
    print("Received '%s'" % result)
    ws.close()

def send_word(event, context):
    # pathParams = json.load(event)
    channel = event['pathParameters']['channel']
    word = event['pathParameters']['word']
    # print(params)
    send_word_to_channel(word,channel) 
    body = {
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
