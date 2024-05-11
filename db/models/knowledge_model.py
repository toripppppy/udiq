"""
Model for knowledge
"""

class KnowledgeModel:
    def __init__(self, id: int, word: str, meaning: str) -> None:
        self.id = id
        self.word = word
        self.meaning = meaning

    def __str__(self) -> str:
        return f"[<KnowledgeModel> word: {self.word}, meaning: {self.meaning}]"

    def get_id(self) -> int:
        return self.id

    def get_word(self) -> str:
        return self.word
    
    def get_meaning(self) -> str:
        return self.meaning