from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .item_type import ItemType

class ItemDataInterface(ABC):
    """Abstract interface for all item data types"""
    
    def __init__(self) -> None:
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    @abstractmethod
    def get_type(self) -> 'ItemType':
        """Return the type of this data"""
        pass
    
    def update_timestamp(self) -> None:
        """Update the timestamp when data is modified"""
        self.updated_at = datetime.now() 