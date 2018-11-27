from db.database_manager import DatabaseManager


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
        cur = self.db_conn.cursor()
        cur.execute("""SELECT * FROM user_to_course uc WHERE uc.user_id = ? AND uc.course_id = ?""",
                    [user_id, course_id])

        results = cur.fetchall()
        cur.close()
        if results is None:
            return []
        return results

    def insert_row(self, user_id, course_id, ratings):

        input_data = [user_id, course_id, ratings["workload_rating"], ratings["recommendation_rating"]]

        cur = self.db_conn.cursor()
        cur.execute('insert into users (user_id, course_id, workload_rating, recommendation_rating) '
                    'values (?,?,?,?,?,?,?,?)', input_data)
        self.db_conn.commit()

    def get_rating(self, user_id, course_id, rating_type):
        cur = self.db_conn.cursor()
        cur.execute("""SELECT ? FROM user_to_course uc WHERE uc.user_id = ? AND uc.course_id = ?""",
                    [rating_type, user_id, course_id])

        results = cur.fetchall()
        cur.close()
        if results is None:
            return []

        return results

    def update_rating(self, user_id, course_id, rating_type, rating_value):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE user_to_course uc SET ?=? WHERE uc.user_id = ? AND uc.course_id = ?""",
                    [rating_type, rating_value, user_id, course_id])

        self.db_conn.commit()
