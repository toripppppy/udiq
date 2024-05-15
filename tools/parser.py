"""
Parser
parse texts in Japanese
"""

import MeCab

class Parser:
    def __init__(self) -> None:
        self.tagger = MeCab.Tagger()
    
    def get_words(self, text: str) -> list[str]:
        par = self.tagger.parseToNode(text)
        words = list()
        while par:
            if par.feature.split(',')[0] in ['名詞', "形容詞", "動詞"]:
                words.append(par.surface)
            par = par.next
        return words