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

    def get_course_data(self, course_code):
        """
        Query courses based on course code 

        :param str course_code: course we are retrieving
        :return:
        """
        cur = self.db_conn.cursor()
        cur.execute("SELECT * FROM course WHERE code=?", [course_code])

        results = cur.fetchall()

        if results is None:
            return []
        return results

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


class _CourseHubDatabaseInitializer:
    """ A set of functions to help setup the database. Use cautiously. """

    def __init__(self):
        self.db_manager = DatabaseManager()
        self.create_tables()

    def insert_course(self, data):
        """ Insert data into the table

        :param dict data: Keys: [courseId, org_name, course_title, code, course_description]
        :return:
        """

        course_id = data["course_id"]
        org_name = data["org_name"]
        course_title = data["course_title"]
        code = data["course_code"]
        course_description = data["course_description"]

        input_data = [course_id, code, course_description, course_title, org_name]

        c = self.db_manager.db_conn.cursor()
        course_exists = c.execute('SELECT * FROM course WHERE id = ?', [course_id])

        if course_exists.fetchone() is None:
            c.execute('insert into course values (?,?,?,?,?)', input_data)

        self.db_manager.db_conn.commit()
        c.close()

    def create_tables(self):
        """ Creates the comment and course tables in the db """

        comment_table = """  CREATE TABLE IF NOT EXISTS comments(
            id integer PRIMARY KEY,
            course text,
            comment text,
            timestamp integer,
            votes integer); 
        """

        course_table = """
        CREATE TABLE IF NOT EXISTS course(
            id integer PRIMARY KEY,
            course_code text,
            course_description text,
            course_title text,
            org_name text);
        """
        self.db_manager.create_table(comment_table)
        self.db_manager.create_table(course_table)
