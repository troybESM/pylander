
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
send_word_to_channel("butts","secret-guesser")