
import ssl
import json
import random
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
def get_random_word():
    wordList = open('words.list').read().split()
    random_word = random.choice(wordList)
    print(f"Random Word is: {random_word}")
    return random_word

def send_word(event, context):
    # pathParams = json.load(event)
    channel = event['pathParameters']['channel']
    # if event['pathParameters']['word']:
    #     word = event['pathParameters']['word']
    # else: 
    word = get_random_word()
    # print(params)
    send_word_to_channel(word,channel) 


    response = {
        "statusCode": 200,
        "headers": {'Access-Control-Allow-Origin': '*','Access-Control-Allow-Credentials': True},
        "body": json.dumps(event)
    }
    return response