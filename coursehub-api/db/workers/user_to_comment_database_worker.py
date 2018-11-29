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
                    FROM user_to_comment uc
                    INNER JOIN comments c ON uc.comment_id = c.id
                    WHERE uc.user_id = ?""", [user_id])

        results = cur.fetchall()
        if results is None:
            return []
        return results

    def insert_row(self, user_id, comment_id):
        """

        :param user_id:
        :type user_id:
        :param comment_id:
        :type comment_id:
        :return:
        :rtype:
        """
        if self.get_rating(user_id, comment_id) is None:

            rating = "None"

            c = self.db_conn.cursor()
            c.execute('insert into user_to_comment(user_id, comment_id, upvote_or_downvote) values(?, ?, ?)',
                      [user_id, comment_id, rating])
            self.db_conn.commit()
            c.close()

    # insert a upvote or donwvote func for logic
    def get_rating(self, user_id, comment_id):
        """Get the upvote or downvote value for a users comment

        :param comment_id:
        :type comment_id:
        :param user_id:
        :type user_id:
        :return:
        """
        cur = self.db_conn.cursor()
        cur.execute("""SELECT upvote_or_downvote FROM user_to_comment WHERE comment_id = ? AND
        user_id = ?""", [comment_id, user_id])

        results = cur.fetchall()
        if results == []:
            return None
        return results[0][0]

    def set_rating(self, user_id, comment_id, value):
        """Set the upvote or downvote value for a users comment to value

        :param comment_id:
        :type comment_id:
        :param user_id:
        :type user_id:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE user_to_comment SET upvote_or_downvote = ? WHERE comment_id = ? AND
                user_id = ?""", [value, comment_id, user_id])

        self.db_conn.commit()
        cur.close()
