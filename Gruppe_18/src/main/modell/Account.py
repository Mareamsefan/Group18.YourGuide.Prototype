import json
import uuid


class Account:

    def __init__(self, username, password, phoneNumber, emailAddress):
        self.username = username
        self.password = password
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.account_id = str(uuid.uuid4())
        self.registered_tours = []

    def get_registered_tours(self):
        return self.registered_tours


