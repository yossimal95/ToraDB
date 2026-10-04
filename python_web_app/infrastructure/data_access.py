import sqlite3
import os

class DataAccess:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_PATH = os.path.join(BASE_DIR, 'db', 'torah.db')

    @staticmethod
    def _get_connection():
        """Creates and returns a connection to the SQLite database."""
        conn = sqlite3.connect(DataAccess.DB_PATH)
        # Allows accessing columns by name
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def execute_read(query, params=()):
        """
        Executes a read (SELECT) query and returns a list of dictionaries.
        """
        try:
            with DataAccess._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except sqlite3.Error as e:
            return {"error": str(e)}

    @staticmethod
    def execute_write(query, params=()):
        """
        Executes a write (INSERT/UPDATE/DELETE) query and returns the number of affected rows.
        """
        try:
            with DataAccess._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            return {"error": str(e)}

    @staticmethod
    def execute_transaction(queries_with_params):
        """
        Executes a list of (query, params) tuples in a single transaction.
        If one fails, the entire transaction is rolled back.
        """
        try:
            with DataAccess._get_connection() as conn:
                cursor = conn.cursor()
                for query, params in queries_with_params:
                    cursor.execute(query, params)
                conn.commit()
                return True
        except sqlite3.Error as e:
            return {"error": str(e)}
