import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def callFromTwilio():
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']
    studio_flow_sid = os.environ['STUDIO_FLOW_SID']

    call_from = os.environ['TWILIO_PHONE_NUMBER']
    call_to = os.environ['CALL_TO']


    client = Client(account_sid, auth_token)
    execution = client.studio.v2.flows(
        studio_flow_sid
    ).executions.create(to=call_to, from_=call_from)

    print("Called", execution.sid)

if __name__ == "__main__":
    callFromTwilio()