import os
import io
import boto3
import json
import base64
from urllib import parse
import re
from twilio.rest import Client

TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print(event)
    
    # Decode body
    body_from_receiving_text = base64.b64decode(event['body'].encode('ascii'))
    body_from_receiving_text = body_from_receiving_text.decode('ascii')
    print(body_from_receiving_text)
    
    # grab the number it was sent from
    number_received_from = re.search('From=%2B(.*)&ApiVersion', body_from_receiving_text)
    print(number_received_from.group(1))
    
    # Grab the message sent
    message_received = re.search('&Body=(.*)&FromCountry', body_from_receiving_text)
    print(message_received.group(1))
    
    # Call the LLM
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                        ContentType='application/json',
                                        Body=json.dumps({
                                         "inputs": [
                                          [
                                           {"role": "system", "content": "You are chat bot who answers questions about general knowledge"},
                                           {"role": "user", "content": message_received.group(1)}
                                          ]
                                         ],
                                         "parameters": {"max_new_tokens":256, "top_p":0.9, "temperature":0.6}
                                        }),
                                      CustomAttributes="accept_eula=true")
    print(response)
    
    result = json.loads(response['Body'].read().decode())
    print(result)
    
    # Params for text to be sent
    to_number = '+' + number_received_from.group(1)
    from_number = '+18665117677'
    body = result[0]["generation"]["content"]

    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not body:
        return "The function needs a 'Body' message to send."

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
    .create(
         body=body,
         from_=from_number,
         to=to_number
     )
    
    return (message.sid)

    # # insert Twilio Account SID into the REST API URL
    # populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    # post_params = {"To": to_number, "From": from_number, "Body": body}

    # # encode the parameters for Python's urllib
    # data = parse.urlencode(post_params).encode()
    # req = request.Request(populated_url)

    # # add authentication header to request based on Account SID + Auth Token
    # authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # base64string = base64.b64encode(authentication.encode('utf-8'))
    # req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    # try:
    #     # perform HTTP POST request
    #     with request.urlopen(req, data) as f:
    #         print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    # except Exception as e:
    #     # something went wrong!
    #     return e

    # return "SMS sent successfully!"
