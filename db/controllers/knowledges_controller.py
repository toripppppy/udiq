"""
Controller for knowledges
"""

from db.db_manager import MariaDBConnector
from db.models.knowledge_model import KnowledgeModel


class KnowledgesController:
    def __init__(self) -> None:
        self.connector = MariaDBConnector()
        self.cursor = self.connector.get_cursor()
        self.conn = self.connector.get_conn()

    def execute_sql(self, sql: str, params=None) -> None:
        print(sql)
        self.cursor.execute(sql, params)

    def find_one_by_id(self, id: int) -> KnowledgeModel | None:
        self.execute_sql("SELECT * FROM knowledges WHERE id = ?", (id,))
        result = tuple(*[knowledge for knowledge in self.cursor])

        if result == ():
            return None
        else:
            return KnowledgeModel(*result[1:])

    def find_all(self) -> tuple[KnowledgeModel] | None:
        self.execute_sql("SELECT * FROM knowledges")
        result = tuple([KnowledgeModel(*knowledge[1:]) for knowledge in self.cursor])

        if result == ():
            return None
        else:
            return result

    def insert_one(self, knowledge: KnowledgeModel) -> str:
        cursor = self.connector.get_cursor()
        self.execute_sql(f'INSERT INTO knowledges (word, meaning) VALUES("{knowledge.word}", "{knowledge.meaning}")')
        cursor.close()
        self.conn.commit()
        return "success"
        
    def delete_one(self, key: str) -> str:
        cursor = self.connector.get_cursor()
        if key in self.get_words():
            self.execute_sql(f'DELETE FROM knowledges WHERE word="{key}"')
            cursor.close()
            self.conn.commit()
            return "success"
        else:
            return "error.notfound"

    def get_words(self) -> str:
        knowledges = self.find_all()
        if knowledges is not None:
            return [kn.word for kn in knowledges]
        else:
            return []
