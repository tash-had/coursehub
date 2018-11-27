from db.database_manager import DatabaseManager, sqlite3


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
        db_conn = sqlite3.connect(self._db_path)
        cur = db_conn.cursor()
        cur.execute("SELECT username FROM users WHERE id=?", [user_id])

        results = cur.fetchall()
        cur.close()
        if results is None:
            return []
        return results

    def add_new_user(self, user):
        user_id = user.id
        username = user.username
        email = user.email
        picture = user.picture

        input_data = [user_id, username, email, picture]

        db_conn = sqlite3.connect(self._db_path)
        c = db_conn.cursor()
        c.execute('insert into users (id, username, email, picture) '
                  'values (?,?,?,?)', input_data)
        db_conn.commit()
