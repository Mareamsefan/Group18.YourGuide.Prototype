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

    def register_to_tour(self, tour):
        if tour.booked < tour.max_travelers:
            tour.book_tour()
            self.registered_tours.append(tour)
        else:
            return "you can't register to this tour"
