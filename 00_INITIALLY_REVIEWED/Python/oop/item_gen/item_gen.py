from sortedcontainers import SortedDict
from datetime import datetime
from models.item import Item
import time

class ItemGenerator:

    def __init__(self) -> None:
        self.items = SortedDict()

    def list_items(self) -> list[Item]:
        return list(self.items.values())

    def __plan_steps(self, item: Item) -> list[str]:
        # AI to decide how many steps are needed to create the item, and what the steps are
        # TODO implement this

        print(f"Planning steps for item: {item.item_id}")
        # Parse number of steps from prompt
        try:
            num_steps = int(item.prompt.split("with ")[1].split(" steps")[0])
        except (IndexError, ValueError):
            raise ValueError("Invalid prompt: 'with' keyword not found")
            
        # adding 1s sleep to simulate the time it takes to plan the steps
        time.sleep(1)
        # Create placeholder steps
        steps = [f"Step {i+1}" for i in range(num_steps)]
        return steps

    def __generate_tags(self, item: Item) -> list[str]:
        # AI to decide what could be applicable tags for the item
        # TODO implement this
        print(f"Generating tags for item: {item.item_id}")
        # Parse tags from prompt
        try:
            tags = item.prompt.split("tags: ")[1].split(",")
        except (IndexError, ValueError):
            raise ValueError("Invalid prompt: 'tags' keyword not found")
        # adding 1s sleep to simulate the time it takes to generate the tags
        time.sleep(1)
        return tags
    
    def create_item(self, prompt: str) -> Item: 
        item_id = f"item_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        item = Item(item_id=item_id, prompt=prompt, status="pending")

        item.set_item_status("planning steps")
        steps = self.__plan_steps(item)
        item.set_steps(steps)

        item.set_item_status("generating tags")
        tags = self.__generate_tags(item)
        item.set_tags(tags)

        item.set_item_status("completed")
        item.updated_at = datetime.now()
        self.items[item.item_id] = item
        return item

    def get_item(self, item_id: str) -> Item:
        return self.items[item_id]

    def share_item(self, item_id: str) -> Item:
        item = self.get_item(item_id)
        item.shared_to_public = True
        return item
    
    def unshare_item(self, item_id: str) -> Item:
        item = self.get_item(item_id)
        item.shared_to_public = False
        return item
    
    def delete_item(self, item_id: str) -> Item:
        item = self.get_item(item_id)
        item.deleted_at = datetime.now()
        return item
    

def main():
    item_gen = ItemGenerator()
    item = item_gen.create_item("Create item with 10 steps and tags: tag1, tag2, tag3")
    print(f"Item {item.item_id} created")

    while item.status != "completed":
        print(f"Item {item.item_id} status: {item.status}")
        time.sleep(1)
    
    print(f"Item {item.item_id} completed")
    print(f"Item {item.item_id} steps: {item.steps}")
    print(f"Item {item.item_id} tags: {item.tags}")

if __name__ == "__main__":
    main()