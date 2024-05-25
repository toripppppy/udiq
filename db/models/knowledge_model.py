"""
Model for knowledge
"""

class KnowledgeModel:
    def __init__(self, word: str, meaning: str) -> None:
        self.word = word
        self.meaning = meaning

    def __str__(self) -> str:
        return f"[<KnowledgeModel> word: {self.word}, meaning: {self.meaning}]"

    def is_valid(self) -> bool:
        # validation
        return self.word != None and self.meaning != None

    