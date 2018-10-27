"""Basic DataBase for a comment"""

import sqlite3
import json
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


def get_from_database(conn, course):
    """
    Query courses based on course
    :param conn: the Connection object
    :param course: course we are retrieving
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM course WHERE code=?", (course,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def insert(conn, json):
    """
    Insert data into the table
    :param conn: the Connection object
    :param json: json file to put in database
    :return:
    """

    data = json.load(open(json))
    conn = sqlite3.connect(conn)

    id = data[0]["courseId"]
    orgName = data[0]["orgName"]
    courseTitle = data[0]["courseTitle"]
    code = data[0]["code"]
    courseDescription = data[0]["courseDescription"]

    input_data = [id, code, courseDescription, courseTitle, orgName]

    c = conn.cursor()
    c.execute('insert into course values (?,?,?,?,?)', input_data)

    conn.commit()
    c.close()


def main():
    """Main function for running and creating database"""
    db = "C:\\Users\culle\Documents\pythonDatabase.db"

    course_db = "C:\\Users\culle\csc301\project\project-team-19\course_db.db"

    comment_database = """  CREATE TABLE IF NOT EXISTS comments(
    id integer PRIMARY KEY,
    course text,
    comment text,
    timestamp text,
    votes integer); """

    course_database = """
    CREATE TABLE IF NOT EXISTS course(
    id text PRIMARY KEY,
    code text,
    courseDescription text,
    courseTitle text,
    orgName text);
    """

    conn = create_connection(db)
    if conn is not None:
        create_table(conn, comment_database)
    else:
        print("Cannot create the database connection.")

    conn_course = create_connection(course_db)
    if conn_course is not None:
        create_table(conn, course_database)
    else:
        print("Cannot create the database connection.")


if __name__ == '__main__':
    main()
