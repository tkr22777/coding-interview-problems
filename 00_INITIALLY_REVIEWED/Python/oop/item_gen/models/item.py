from datetime import datetime

"""
Item Relationship Diagram:
Item
 |
 |-- steps [list]
 |    |-- step 1
 |    |-- step 2 
 |    `-- step N
 |
 |-- tags  [ tagA, tagB, tagC ]
 `-- status [ pending, processing, validating, completed ]
"""

class Item:
    def __init__(self, item_id: str, prompt: str, status: str) -> None:
        self.item_id = item_id

        # high priority
        self.steps = None
        self.item_data = None  # Will be set later by ItemGenerator
        self.prompt = prompt
        self.status = status

        # low priority
        self.tags = None
        self.shared_to_public = False
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.deleted_at = None

    def set_steps(self, steps: list) -> 'Item':
        self.steps = steps
        self.updated_at = datetime.now()
        return self
    
    def set_item_status(self, status: str) -> 'Item':
        # set the status of the item
        self.status = status
        self.updated_at = datetime.now()
        return self
    
    def set_item_data(self, item_data) -> 'Item':
        # set the item data (type + data together)
        # Using generic type to avoid circular import
        self.item_data = item_data
        self.updated_at = datetime.now()
        return self

    # low priority
    def set_tags(self, tags: list) -> 'Item':
        self.tags = tags
        self.updated_at = datetime.now()
        return self

