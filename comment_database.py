"""Basic DataBase for a comment"""

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database
     :param db_file: Database file
     :rtype {cursor}
     """
    global connection
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)


def create_table(conn, instructions):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param instructions: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        return c.execute(instructions)
    except Error as e:
        print(e)

    return None


def main():
    """Main function for running and creating database"""
    db = "C:\\Users\culle\Documents\pythonDatabase.db"

    comment_database = """  CREATE TABLE IF NOT EXISTS comments(
    id integer PRIMARY KEY,
    course text,
    comment text,
    timestamp text,
    votes integer); """

    conn = create_connection(db)
    if conn is not None:
        create_table(conn, comment_database)
    else:
        print("Cannot create the database connection.")


if __name__ == '__main__':
    main()
