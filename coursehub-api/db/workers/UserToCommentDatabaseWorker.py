from db.database_manager import DatabaseManager


class UserToCommentDatabaseWorker(DatabaseManager):
    """Contains the functions for the User to comment database"""

    def __init__(self):
        DatabaseManager.__init__(self)

    def get_all_comments_from_user(self, user_id):
        """
        Get all the comments for a given user id.

        :param user_id:
        :return:
        """
        cur = self.db_conn.cursor()
        cur.execute("""SELECT c.id,
                    FROM user_to_comment_table uc
                    INNER JOIN comments c ON uc.comment_id = c.id
                    WHERE uc.user_id = ?""", [user_id])

        results = cur.fetchall()
        if results is None:
            return []
        return results


