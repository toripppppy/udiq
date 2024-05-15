"""
Controller for knowledges
"""

from db.db_manager import MariaDBConnector
from db.models.knowledge_model import KnowledgeModel

class KnowledgesController:
	def __init__(self) -> None:
		self.connector =  MariaDBConnector()
		self.cursor = self.connector.get_cursor()
		self.conn = self.connector.get_conn()

	def execute_sql(self, sql: str, params = None) -> None:
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
		
	def insert_one(self, knowledge: KnowledgeModel) -> None:
		if knowledge.is_valid() == False: return
		cursor = self.connector.get_cursor()
		self.execute_sql(f'INSERT INTO knowledges (word, meaning) VALUES("{knowledge.word}", "{knowledge.meaning}")')
		cursor.close()
		self.conn.commit()