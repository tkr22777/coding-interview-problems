from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def check_credit(self, user_id: str):
        pass

class CapBank(Bank):
    def __init__(self):
        print("initialzied")
    
    def check_credit(self, user_id: str):
        print(f"credit score of user: {user_id}, score: {1}")

bank = CapBank()
bank.check_credit(user_id="tkr22777")
