from datetime import datetime
from .data_point import DataPoint
from .item_data_interface import ItemDataInterface
from .item_type import ItemType

class ItemTabularData(ItemDataInterface):
    def __init__(self, column_headers: list[str], row_headers: list[str], data: list[list[DataPoint]]) -> None:
        super().__init__()
        self.column_headers = column_headers
        self.row_headers = row_headers
        self.data = data
    
    def get_type(self) -> ItemType:
        """Return TABULAR type"""
        return ItemType.TABULAR
    
    def get_tabular_data(self) -> list[list[DataPoint]]:
        """Get the tabular data matrix - specific to ItemTabularData"""
        return self.data
    
    def get_column_headers(self) -> list[str]:
        """Get column headers"""
        return self.column_headers
    
    def get_row_headers(self) -> list[str]:
        """Get row headers"""
        return self.row_headers
    
    def get_cell(self, row: int, col: int) -> DataPoint:
        """Get a specific cell data point"""
        return self.data[row][col]
    
    def set_cell(self, row: int, col: int, data_point: DataPoint) -> 'ItemTabularData':
        """Set a specific cell data point"""
        self.data[row][col] = data_point
        self.update_timestamp()
        return self
    
    def get_dimensions(self) -> tuple[int, int]:
        """Get (rows, columns) dimensions"""
        return (len(self.data), len(self.data[0]) if self.data else 0) 