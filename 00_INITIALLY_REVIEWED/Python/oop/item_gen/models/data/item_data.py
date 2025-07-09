from datetime import datetime
from .item_data_interface import ItemDataInterface
from .item_type import ItemType

class ItemData:
    """Wrapper class that holds any ItemDataInterface implementation"""
    
    def __init__(self, data_implementation: ItemDataInterface) -> None:
        self.data_implementation = data_implementation
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def get_type(self) -> ItemType:
        """Delegate to the underlying implementation"""
        return self.data_implementation.get_type()
    
    def get_data_implementation(self) -> ItemDataInterface:
        """Get the underlying data implementation"""
        return self.data_implementation
    
    def is_list_data(self) -> bool:
        """Check if this is list data"""
        return self.get_type() == ItemType.LIST
    
    def is_tabular_data(self) -> bool:
        """Check if this is tabular data"""
        return self.get_type() == ItemType.TABULAR
    
    def update_data_implementation(self, data_implementation: ItemDataInterface) -> None:
        """Replace the data implementation"""
        self.data_implementation = data_implementation
        self.updated_at = datetime.now() 