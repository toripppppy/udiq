"""
Connector for MariaDB
"""

import mariadb
import sys

class MariaDBConnector:
    def __init__(self) -> None:   
        # Connect to MariaDB Platform
        try:
            conn = mariadb.connect(
                user="root",
                password="udiqpass",
                host="localhost",
                port=3306,
                database="test"
            )

            self.cursor = conn.cursor()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    # Get Cursor
    def get_cursor(self) -> mariadb.Cursor:
        return self.cursor
    
    # def get_all_knowledges(self) -> tuple[tuple[str]]:
    #     self.cursor.execute("SELECT * FROM knowledges")
    #     return tuple([knowledge for knowledge in self.cursor])