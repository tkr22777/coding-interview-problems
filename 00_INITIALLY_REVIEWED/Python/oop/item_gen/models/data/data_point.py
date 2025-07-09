from datetime import datetime
import uuid

class DataPoint:
    def __init__(self, parent_id: str, prompt: str, sources: list[str]) -> None:
        self.id = str(uuid.uuid4())
        self.parent_id = parent_id # id of the parent data point

        self.value = None # value of the data point
        self.prompt = prompt # prompt used to generate the data point
        self.sources = sources # list of model names
        self.source_confidence_scores = None # list of confidence scores for each source
        self.confidence_score = None # 0-100 (average of source_confidence_scores)

        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def set_value(self, value: str) -> 'DataPoint':
        self.value = value
        self.updated_at = datetime.now()
        return self
    
    def set_source_confidence_scores(self, source_confidence_scores: list[int]) -> 'DataPoint':
        self.source_confidence_scores = source_confidence_scores
        self.updated_at = datetime.now()
        return self
    
    def set_confidence_score(self, confidence_score: int) -> 'DataPoint':
        self.confidence_score = confidence_score
        self.updated_at = datetime.now()
        return self 