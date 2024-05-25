"""
Connector for MariaDB
"""

import mariadb
import sys

class MariaDBConnector:
    def __init__(self) -> None:   
        # Connect to MariaDB Platform
        try:
            self.conn = mariadb.connect(
                user="root",
                password="udiqpass",
                host="localhost",
                port=3306,
                database="test"
            )

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    # Get Cursor
    def get_cursor(self) -> mariadb.Cursor:
        return self.conn.cursor()
    
    def get_conn(self) -> mariadb.Connection:
        return self.conn