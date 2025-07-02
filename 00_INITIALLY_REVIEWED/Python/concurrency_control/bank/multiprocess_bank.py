import multiprocessing as mp
from multiprocessing import Manager
from typing import Dict
from bank.bank_interface import BankInterface, InvalidUserException, UserExistsException, InsufficientFundsException

class MultiprocessBank(BankInterface):
    def __init__(self, users: Dict, balances: Dict, user_locks: Dict, global_lock: mp.Lock) -> None:
        """Initialize bank with shared state for multiprocess use."""
        self.users = users
        self.__users_balance = balances
        self.user_locks = user_locks
        self.global_lock = global_lock

    def add_user(self, user_id: str) -> str:
        with self.global_lock:
            if user_id in self.users:
                raise UserExistsException(f"{user_id} already exists")
            self.users[user_id] = True
            self.__users_balance[user_id] = 0
            print(f"user added: {user_id}")
            return user_id

    def deposit(self, user_id: str, amount: float) -> None:
        if user_id not in self.users:
            raise InvalidUserException(f"{user_id} doesn't exist")

        with self.user_locks[user_id]:  # Use user-specific lock
            current_balance = self.__users_balance[user_id]
            self.__users_balance[user_id] = current_balance + amount
            print(f"deposited user_id: {user_id}, amount: {amount}, current_balance: {self.__users_balance[user_id]}")

    def withdraw(self, user_id: str, amount: float) -> float:
        if user_id not in self.users:
            raise InvalidUserException(f"{user_id} doesn't exist")

        with self.user_locks[user_id]:  # Use user-specific lock
            current_balance = self.__users_balance[user_id]
            if current_balance < amount:
                raise InsufficientFundsException(
                    f"Insufficient funds for {user_id}. "
                    f"Required: ${amount}, Available: ${current_balance}"
                )
            self.__users_balance[user_id] = current_balance - amount
            print(f"withdrawn user_id: {user_id}, amount: {amount}, current_balance: {self.__users_balance[user_id]}")
            return amount

    def transfer(self, from_user_id: str, to_user_id: str, amount: float) -> None:
        if from_user_id == to_user_id:
            raise ValueError("Cannot transfer money to the same account")
            
        if from_user_id not in self.users:
            raise InvalidUserException(f"Source user {from_user_id} doesn't exist")
            
        if to_user_id not in self.users:
            raise InvalidUserException(f"Target user {to_user_id} doesn't exist")

        # Acquire locks in a consistent order to prevent deadlocks
        first_lock = min(from_user_id, to_user_id)
        second_lock = max(from_user_id, to_user_id)
        
        with self.user_locks[first_lock], self.user_locks[second_lock]:
            if self.__users_balance[from_user_id] < amount:
                raise InsufficientFundsException(
                    f"Insufficient funds for transfer from {from_user_id}. "
                    f"Required: ${amount}, Available: ${self.__users_balance[from_user_id]}"
                )
            
            self.__users_balance[from_user_id] -= amount
            self.__users_balance[to_user_id] += amount
            print(
                f"Transferred ${amount} from {from_user_id} (balance: ${self.__users_balance[from_user_id]}) "
                f"to {to_user_id} (balance: ${self.__users_balance[to_user_id]})"
            )

    def get_balance(self, user_id: str) -> float:
        """Get the current balance for a user.
        This is a lock-free operation since reading a float is atomic in Python.
        However, we need to handle the case where the user might not exist.
        """
        # First check if user exists to avoid KeyError
        if user_id not in self.users:
            raise InvalidUserException(f"{user_id} doesn't exist")
            
        try:
            # Direct read without lock - atomic operation
            return self.__users_balance[user_id]
        except KeyError:
            # Handle race condition where user was deleted after our check
            raise InvalidUserException(f"{user_id} was removed")

    def list_users(self) -> list[str]:
        return list(self.users.keys()) 