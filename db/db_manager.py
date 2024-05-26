import mariadb
import os
import sys

class MariaDBConnector:
    def __init__(self) -> None:
        # Connect to MariaDB Platform
        try:
            self.conn = mariadb.connect(
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=int(os.getenv('DB_PORT')),
                database=os.getenv('DB_NAME')
            )

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    # Get Cursor
    def get_cursor(self) -> mariadb.Cursor:
        return self.conn.cursor()

    def get_conn(self) -> mariadb.Connection:
        return self.conn