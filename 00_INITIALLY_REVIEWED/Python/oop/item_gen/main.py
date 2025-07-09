from item_gen import ItemGenerator
import time

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
    
    # Show the new ItemData functionality
    if item.item_data:
        print(f"Item data type: {item.item_data.get_type()}")
        print(f"Is list data: {item.item_data.is_list_data()}")
        if item.item_data.is_list_data():
            list_data = item.item_data.get_list_data()
            print(f"List data contains {len(list_data.list_data)} data points")
            for i, dp in enumerate(list_data.list_data):
                print(f"  Data point {i+1}: {dp.value}")

if __name__ == "__main__":
    main() 