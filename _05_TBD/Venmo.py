import bisect
import time
from collections import defaultdict
import threading
import datetime as dt
import random
import string

class ExcessiveWithdrawalAttemptsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Venmo:
    def __init__(self):
        self.users_balance = defaultdict(int)
        self.users_metadata = defaultdict(lambda: [10])  # (init max transfer limit)
        self.withdrawals = defaultdict(list)
        self.locks = defaultdict(threading.Lock)
        self.lock = threading.Lock()

    def create_user(self, name: str) -> bool:
        with self.lock:
            if name in self.users_balance:
                raise ValueError("the user already exist")

            self.users_balance[name] = 0
        return True

    def set_max_withdraw_limit(self, name: str, amount: int) -> bool:
        with self.locks[name]:
            self.users_metadata[name][0] = amount
        return True

    def deposit(self, name: str, amount: int) -> bool:
        if amount <= 0:
            raise ValueError("the amount to deposit to the account must be positive")

        if name not in self.users_balance:
            raise ValueError("user:{} do not have an account".format(name))

        with self.locks[name]:
            self.users_balance[name] += amount
        return True

    def add_withdrawal_record(self, name: str, txn_id: str, amount: int) -> bool:
        with self.locks[name]:
            self.withdrawals[name].append((txn_id, amount, dt.datetime.now()))
        return True

    def recent_transaction_count(self, name: str, seconds: int) -> int:
        with self.locks[name]:
            print(self.withdrawals[name])
            ts_withdrawals = [w[2] for w in self.withdrawals[name]]
            print(self.withdrawals[name])

        print(ts_withdrawals)
        end_time = dt.datetime.now()
        start_time = end_time - dt.timedelta(seconds=seconds)

        i = bisect.bisect_left(ts_withdrawals, start_time)
        j = bisect.bisect_right(ts_withdrawals, end_time)

        return j - i

    def withdraw(self, name: str, amount: int) -> bool:
        if amount <= 0:
            raise ValueError("the amount to withdraw from the account must be positive")

        with self.locks[name]:
            max_amount = self.users_metadata[name][0]
            if amount > max_amount:
                raise ValueError("user is not allowed to withdraw more than:{} ".format(max_amount))

            if self.users_balance[name] < amount:
                raise ValueError("there's insufficient balance on the account to remove from")

            self.users_balance[name] -= amount
        return True

    def transfer(self, sender: str, receiver: str, amount: int) -> bool:
        seconds = 5
        txn_count = self.recent_transaction_count(sender, seconds)
        print("{}'s latest transaction count: {}".format(sender, txn_count))
        if txn_count > 2:
            raise ExcessiveWithdrawalAttemptsError("Excessive withdrawal attempts:{}".format(txn_count))
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        txn_id = "txn_" + random_id + ": " + sender + "_to_" + receiver
        self.withdraw(sender, amount)
        self.add_withdrawal_record(sender, txn_id, amount)
        self.deposit(receiver, amount)
        return True

    def print(self):
        print("__________")
        print("Bank info:")
        print("----------")
        for user in self.users_balance:
            print("User:" + user + " \tAccount balance:" + str(self.users_balance[user]))
            print("User:" + user + " \tMax withdrawal limit:" + str(self.users_metadata[user][0]))
            if user in self.withdrawals:
                print("User:" + user + " \tRecent withdrawals:")
                for wd in self.withdrawals[user]:
                    print(wd)
            print()


venmo = Venmo()
venmo.create_user("tahsin")
venmo.create_user("ana")
venmo.create_user("dunya")
venmo.create_user("maddie")
venmo.deposit("tahsin", 1000)

try:
    venmo.deposit("unknown", 100)
except Exception as e:
    print("unable to add user unknown, exception message:" + str(e))

venmo.deposit("dunya", 100)
venmo.deposit("ana", 100)
venmo.set_max_withdraw_limit("tahsin", 100)
venmo.set_max_withdraw_limit("dunya", 40)

venmo.print()
venmo.transfer("dunya", "tahsin", 30)
venmo.transfer("tahsin", "dunya", 100)
venmo.transfer("tahsin", "dunya", 100)
venmo.transfer("tahsin", "ana", 100)
venmo.print()
try:
    venmo.transfer("tahsin", "maddie", 200)
except Exception as e:
    print("unable to transfer:" + str(e))

time.sleep(5)
venmo.transfer("tahsin", "maddie", 100)
venmo.print()
venmo.transfer("dunya", "tahsin", 30)
venmo.print()

# features to add, make sure you only allow a max of 4 withdrawals per 10 secs
print(venmo.recent_transaction_count("tahsin", 10))