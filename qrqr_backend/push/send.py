import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred_path = ""
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

registration_token = ''
message = messaging.Message(
    notification = messaging.Notification(
        title='title',
        body='body'
    ),
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)