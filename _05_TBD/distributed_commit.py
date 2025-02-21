from datetime import datetime
import random
import string
import json

# functionalities: 
# store a document 
# index by creation_date, weight
# fault tolerance if failure occurs amidst writing te multiple data structures
# lamport clock for detecting unintended, faulty writes

# retrieve a document by id
# retrieve a list of document within a range using pagination

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)

class Document():
    def __init__(self, content: str, creation_date: datetime, weight: int) -> None:
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        self.id = "doc_" + random_id
        self.content = content
        self.creation_date = creation_date
        self.weight = weight

    def __str__(self) -> str:
        return json.dumps(self, cls=MyEncoder)

class DocumentStore:
    def __init__(self) -> None:
        self.kv = {}

    def store(self, document: Document):
        self.kv[document.id] = document

    def get(self, id: str):
        return self.kv[id]
    
print("test")
ds = DocumentStore()
doc_01 = Document("some", None, 1)
print(doc_01)
