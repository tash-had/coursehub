"""Basic DataBase for a comment"""

import sqlite3
from sqlite3 import Error


class DatabaseManager:
    """ The medium through which one should communicate to the db """
    def __init__(self, db_name="coursehub.db"):
        import os
        base_path = os.path.dirname(os.path.abspath(__file__)) + "/"
        self._db_path = base_path + db_name
        self.db_conn = sqlite3.connect(self._db_path)
        if self.db_conn is None:
            raise sqlite3.DatabaseError("Could not establish a connection to the database.")

    def create_table(self, instructions):
        """ create a table from the create_table_sql statement
        :param instructions: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.db_conn.cursor()
            return c.execute(instructions)
        except Error as e:
            print(e)
        return None
