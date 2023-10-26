from Gruppe_18.src.main.repository.JSONRepository import JSONRepository
from Gruppe_18.src.main.model.models import Account, Tour

from Gruppe_18.src.main.model.models import tour_account_association


class AccountRepository(JSONRepository):

    def __init__(self, session):
        self.session = session

    def delete_account(self, session, entity):
        account_to_delete = session.query(Account).filter_by(username=entity.username).first()

        if account_to_delete:
            session.delete(account_to_delete)
            session.commit()
            return True

        return False


    def successful_registration(self, entity, io_stream):
        self.save_to_stream(entity, io_stream)
        return True

    def create_account(self, entity):
        account = Account(username=entity.username,
                          password=entity.password,
                          phoneNumber=entity.phoneNumber,
                          emailAddress=entity.emailAddress)

        self.session.add(account)
        self.session.commit()
        return account

    def account_register_to_tour(self, tour_id, user_id):
        tour = self.session.query(Tour).filter_by(tour_id=tour_id).first()
        user = self.session.query(Account).filter_by(account_id=user_id).first()

        if tour is not None and user is not None:
            tour_account_assoc_obj = tour_account_association.insert().values(
                tour_id=tour_id,
                account_id=user_id
            )
            self.session.execute(tour_account_assoc_obj)
            self.session.commit()
        else:
            print("Tur eller bruker ble ikke funnet.")