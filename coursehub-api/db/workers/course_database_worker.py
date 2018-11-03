from db.database_manager import DatabaseManager, sqlite3


class CourseDatabaseWorker(DatabaseManager):
    """Updates and gets course information in the course database"""

    def __init__(self):
        DatabaseManager.__init__(self)

    def get_courses_data(self, course_code):
        """
        Query courses based on partial (or complete) course code

        :param str course_code: courses we are retrieving
        :return:
        """
        db_conn = sqlite3.connect(self._db_path)
        cur = db_conn.cursor()

        query_str = "SELECT * FROM courses WHERE course_code LIKE '%" + course_code + "%'"

        cur.execute(query_str)

        results = cur.fetchall()
        cur.close()
        if results is None:
            return []
        return results

    def get_course_by_id(self, id_):
        """
        Query courses based on course id
        :param int id_: course to retrieve
        :return:
        """
        db_conn = sqlite3.connect(self._db_path)
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM courses WHERE id=?", [id_])

        results = cur.fetchall()
        if results is None:
            return []
        return results

    def update_course_field(self, id_, field, new_value):
        """
        Update the field 'field' in course specified by 'id_' to 'new_value'
        :param id_: str
        :param field: str
        :param new_value: int or str
        :return: nothing!
        """
        db_conn = sqlite3.connect(self._db_path)
        cur = db_conn.cursor()

        query_str = "UPDATE courses SET " + field + " = " + str(new_value) + " WHERE id=?"
        cur.execute(query_str, [id_])
        db_conn.commit()