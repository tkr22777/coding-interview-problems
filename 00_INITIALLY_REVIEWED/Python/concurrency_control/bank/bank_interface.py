from abc import ABC, abstractmethod
from typing import List

class InvalidUserException(Exception):
    pass

class UserExistsException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class BankInterface(ABC):
    @abstractmethod
    def add_user(self, user_id: str) -> str:
        """Add a new user to the bank.
        
        Args:
            user_id: Unique identifier for the user (min 8 chars)
            
        Returns:
            The user_id if successfully added
            
        Raises:
            UserExistsException: If user_id already exists
            ValueError: If user_id is less than 8 chars
        """
        pass
    
    @abstractmethod
    def deposit(self, user_id: str, amount: float) -> None:
        """Deposit money into user's account.
        
        Args:
            user_id: The user to deposit money for
            amount: Amount to deposit
            
        Raises:
            InvalidUserException: If user_id doesn't exist
        """
        pass
    
    @abstractmethod
    def withdraw(self, user_id: str, amount: float) -> float:
        """Withdraw money from user's account.
        
        Args:
            user_id: The user to withdraw money from
            amount: Amount to withdraw
            
        Returns:
            The amount withdrawn
            
        Raises:
            InvalidUserException: If user_id doesn't exist
            InsufficientFundsException: If user doesn't have enough balance
        """
        pass

    @abstractmethod
    def get_balance(self, user_id: str) -> float:
        """Get the current balance of a user.
        
        Args:
            user_id: The user whose balance to check
            
        Returns:
            The current balance
            
        Raises:
            InvalidUserException: If user_id doesn't exist
        """
        pass

    @abstractmethod
    def transfer(self, from_user_id: str, to_user_id: str, amount: float) -> None:
        """Transfer money from one user to another.
        
        Args:
            from_user_id: The user to transfer money from
            to_user_id: The user to transfer money to
            amount: Amount to transfer
            
        Raises:
            InvalidUserException: If either user_id doesn't exist
            InsufficientFundsException: If from_user doesn't have enough balance
            ValueError: If from_user and to_user are the same
        """
        pass
    
    @abstractmethod
    def list_users(self) -> List[str]:
        """List all users in the bank.
        
        Returns:
            List of user IDs
        """
        pass 