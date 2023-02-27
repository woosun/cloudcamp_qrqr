import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred_path = "qrqr-c2114-firebase-adminsdk-4ukxi-da08676880.json"
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

registration_token = 'BHBcJLTFsZIYp9e6TFHbqJ7PRbhmvnxR8S2BBASR2wIW2xmkDSIs0AU6Ik_BwznRGlLm4LsxvHDD7pWOAyLiNgc'
message = messaging.Message(
    notification = messaging.Notification(
        title='title',
        body='body'
    ),
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)