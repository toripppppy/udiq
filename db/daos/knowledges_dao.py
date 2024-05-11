"""
DAO for knowledges
"""

import sys
sys.path.append("~/db")

from db.db_manager import MariaDBConnector
from db.models.knowledge_model import KnowledgeModel

class KnowledgesDAO:
	def __init__(self) -> None:
		self.cursor = MariaDBConnector().get_cursor()

	def execute_sql(self, sql: str, params = None) -> None:
		self.cursor.execute(sql, params)

	def find_one_by_id(self, id: int) -> KnowledgeModel:
		self.execute_sql("SELECT * FROM knowledges WHERE id = ?", (id,))
		result = tuple(*[knowledge for knowledge in self.cursor])
		
		if result == ():
			return None
		else:
			return KnowledgeModel(*result)
		
	def find_all(self) -> KnowledgeModel:
		self.execute_sql("SELECT * FROM knowledges")
		result = tuple([knowledge for knowledge in self.cursor])

		if result == ():
			return None
		else:
			return result
