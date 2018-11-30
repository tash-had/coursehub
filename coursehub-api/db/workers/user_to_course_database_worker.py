from db.database_manager import DatabaseManager, sqlite3


class UserToCourseDatabaseWorker(DatabaseManager):
    """Contains the functions for the User to comment database"""

    def __init__(self):
        DatabaseManager.__init__(self)

    def get_row(self, user_id, course_id):
        """
        Get the row for a given user id and course id.

        :param user_id:
        :param course_id:
        :return:
        """
        cur = sqlite3.connect(self._db_path).cursor()
        cur.execute("""SELECT * FROM user_to_course uc WHERE uc.user_id = ? AND uc.course_id = ?""",
                    [user_id, course_id])

        results = cur.fetchall()
        cur.close()
        if results is None:
            return []
        return results

    def insert_row(self, user_id, course_id, ratings):

        input_data = [user_id, course_id, ratings["workload_rating"], ratings["recommendation_rating"]]

        db_conn = sqlite3.connect(self._db_path)
        cur = db_conn.cursor()
        cur.execute('insert into user_to_course (user_id, course_id, workload_rating, recommendation_rating) '
                    'values (?,?,?,?)', input_data)
        db_conn.commit()
        cur.close()

    def get_rating(self, user_id, course_id, rating_type):
        cur = sqlite3.connect(self._db_path).cursor()
        cur.execute("""SELECT ? FROM user_to_course uc WHERE uc.user_id = ? AND uc.course_id = ?""",
                    [rating_type, user_id, course_id])

        results = cur.fetchall()
        cur.close()
        if results is None:
            return []

        return results

    def update_rating(self, user_id, course_id, rating_type, rating_value):
        db_conn = sqlite3.connect(self._db_path)
        cur = db_conn.cursor()
        query_str1 = "UPDATE user_to_course SET " + rating_type + " = " + str(rating_value)
        query_str2 = " WHERE user_id = ? AND course_id = " + course_id
        query = query_str1 + query_str2
        cur.execute(query, [user_id])

        db_conn.commit()
