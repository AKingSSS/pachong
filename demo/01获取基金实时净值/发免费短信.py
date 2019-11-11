# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC0b564bd37583e9a387a6297d1ab4****'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_='+1501712****',
    to='+1555867****'
)

print(message.sid)