from db.database_manager import DatabaseManager


class UserDatabaseWorker(DatabaseManager):
    """Contains the functions for the User database"""

    def __init__(self):
        DatabaseManager.__init__(self)

    def get_username_by_id(self, user_id):
        """
        Get the username for a specific user

        :param str user_id: user we want the username for
        :return:
        """
        cur = self.db_conn.cursor()
        cur.execute("SELECT username FROM users WHERE id=?", [user_id])

        results = cur.fetchall()
        if results is None:
            return []
        return results
