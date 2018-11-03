from db.database_manager import DatabaseManager


class CommentDatabaseWorker(DatabaseManager):
    """Contains the functions to add to and retrieve from the database"""

    def __init__(self):
        DatabaseManager.__init__(self)

    def insert_comment(self, data):
        """ Insert data into the comments table

        :param dict data: Keys: [id, course_id, comment, timestamp, votes]
        :return:
        """

        comment_id = data["id"]
        course_id = data["course_id"]
        comment = data["comment"]
        time = data["timestamp"]
        votes = data["votes"]

        input_data = [comment_id, course_id, comment, time, votes]

        c = self.db_conn.cursor()
        c.execute('insert into comments (id, course_id, comment, timestamp, votes) values (?,?,?,?,?)', input_data)
        self.db_conn.commit()
        c.close()

    def get_comments_for_course(self, course_id):
        """
        Get all comments for a specific course

        :param str course_id: course we are retrieving data for
        :return:
        """
        cur = self.db_conn.cursor()
        cur.execute("SELECT * FROM comments WHERE course_id=?", [course_id])

        results = cur.fetchall()
        if results is None:
            return []
        return results

    def get_comment_by_id(self, comment_id):
        """Return the comment in the database that corresponds to comment_id.

        :param comment_id:
        :return:
        """
        cur = self.db_conn.cursor()
        comment = cur.execute('SELECT * FROM comments WHERE id=?', [comment_id]).fetchone()

        cur.close()
        return comment

    def upvote(self, comment_id):
        """Increment the vote count for the comment by one.

        :param comment_id:
        :return: new score
        """
        # update the comment with comment_id by a value of 1

        cur = self.db_conn.cursor()
        current_votes = cur.execute('SELECT votes FROM comments WHERE id=?', [comment_id]).fetchone()
        cur.execute('UPDATE comments SET votes=? WHERE id=?', [current_votes[0] + 1, comment_id])
        self.db_conn.commit()

        return current_votes[0] + 1

    def downvote(self, comment_id):
        """Decrement the vote count for the comment by one.

        :param comment_id:
        :return: new score
        """
        # update the comment with comment_id by decreasing by a value of 1

        cur = self.db_conn.cursor()
        current_votes = cur.execute('SELECT votes FROM comments WHERE id=?', [comment_id]).fetchone()
        cur.execute('UPDATE comments SET votes=? WHERE id=?', [current_votes[0] - 1, comment_id])
        self.db_conn.commit()

        return current_votes[0] - 1