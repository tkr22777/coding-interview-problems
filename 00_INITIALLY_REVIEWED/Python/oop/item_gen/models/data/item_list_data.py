from datetime import datetime
from .data_point import DataPoint
from .item_data_interface import ItemDataInterface
from .item_type import ItemType

class ItemListData(ItemDataInterface):
    def __init__(self, list_data: list[DataPoint]) -> None:
        super().__init__()
        self.list_data = list_data
    
    def get_type(self) -> ItemType:
        """Return LIST type"""
        return ItemType.LIST
    
    def get_list_data(self) -> list[DataPoint]:
        """Get the list of data points - specific to ItemListData"""
        return self.list_data
    
    def add_data_point(self, data_point: DataPoint) -> 'ItemListData':
        """Add a new data point to the list"""
        self.list_data.append(data_point)
        self.update_timestamp()
        return self
    
    def remove_data_point(self, data_point_id: str) -> 'ItemListData':
        """Remove a data point by ID"""
        self.list_data = [dp for dp in self.list_data if dp.id != data_point_id]
        self.update_timestamp()
        return self
    
    def get_data_point_count(self) -> int:
        """Get the number of data points"""
        return len(self.list_data) 