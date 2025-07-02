from collections import defaultdict
import threading
from threading import Lock
from typing import Dict
from bank.bank_interface import (
    BankInterface, 
    InvalidUserException, 
    UserExistsException,
    InsufficientFundsException
)

class ThreadedBank(BankInterface):
    def __init__(self) -> None:
        self.users: Dict[str, bool] = defaultdict(lambda: True)
        self.__users_balance: Dict[str, float] = defaultdict(lambda: 0)
        self.lock: Dict[str, Lock] = defaultdict(Lock)
        
    def add_user(self, user_id: str) -> str:
        if len(user_id) < 8:
            raise ValueError("user_id must be at least 8 chars")

        with self.lock[user_id]:
            if user_id in self.users:
                raise UserExistsException(f"{user_id} already exists")
            else:
                self.users[user_id]
                self.__users_balance[user_id]

        print(f"user added: {user_id}")
        return user_id
    
    def deposit(self, user_id: str, amount: float) -> None:
        if user_id not in self.users:
            raise InvalidUserException(f"{user_id} doesn't exist")

        with self.lock[user_id]:
            self.__users_balance[user_id] += amount
            print(f"deposited user_id: {user_id}, amount: {amount}, current_balance: {self.__users_balance[user_id]}")
    
    def withdraw(self, user_id: str, amount: float) -> float:
        if user_id not in self.users:
            raise InvalidUserException(f"{user_id} doesn't exist")

        with self.lock[user_id]:
            if self.__users_balance[user_id] < amount:
                raise InsufficientFundsException(
                    f"Insufficient funds for {user_id}. "
                    f"Required: ${amount}, Available: ${self.__users_balance[user_id]}"
                )
            self.__users_balance[user_id] -= amount
            print(f"withdrawn user_id: {user_id}, amount: {amount}, current_balance: {self.__users_balance[user_id]}")
            return amount

    def get_balance(self, user_id: str) -> float:
        if user_id not in self.users:
            raise InvalidUserException(f"{user_id} doesn't exist")
            
        with self.lock[user_id]:
            return self.__users_balance[user_id]
    
    def transfer(self, from_user_id: str, to_user_id: str, amount: float) -> None:
        if from_user_id == to_user_id:
            raise ValueError("Cannot transfer money to the same account")
            
        if from_user_id not in self.users:
            raise InvalidUserException(f"Source user {from_user_id} doesn't exist")
            
        if to_user_id not in self.users:
            raise InvalidUserException(f"Target user {to_user_id} doesn't exist")

        # Lock both accounts in a consistent order to prevent deadlocks
        first_lock = min(from_user_id, to_user_id)
        second_lock = max(from_user_id, to_user_id)
        
        with self.lock[first_lock]:
            with self.lock[second_lock]:
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
    
    def list_users(self) -> list[str]:
        return list(self.users.keys()) 