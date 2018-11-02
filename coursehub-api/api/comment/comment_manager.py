import time
import uuid

from api.comment.comment import Comment
from db.database_manager import CommentdatabaseWorker


class CommentManager:
    def create_comment(self, course_id, text):
        """

        @type course_id: str
        @type text: str
        @rtype: comment
        """
        comment_database_worker = CommentdatabaseWorker()
        comment_id = str(uuid.uuid4())
        time_stamp = time.time()
        data = {"id": comment_id, "course_id": course_id, "comment": text,
                "timestamp": time_stamp, "votes": 1}
        comment_database_worker.insert_comment(data)
        return Comment(1, text, time_stamp, course_id, comment_id)

    def get_comments_by_course(self, course_id):
        """

        @type course_id: str
        @rtype: comment[]
        """
        comment_database_worker = CommentdatabaseWorker()
        return comment_database_worker.get_comments_for_course(course_id)

    def get_comment_by_id(self, comment_id):
        """

        @type comment_id: str
        @rtype: comment
        """
        comment_database_worker = CommentdatabaseWorker()
        result = comment_database_worker.get_comment_by_id(comment_id)
        return Comment(result[4], result[2], result[3], result[1], result[0])

    def upvote(self, comment_id):
        """
        @type comment_id: str
        @rtype: comment

        """
        comment_database_worker = CommentdatabaseWorker()
        comment_to_upvote = self.get_comment_by_id(comment_id)
        comment_to_upvote.set_score(comment_database_worker.upvote(comment_id))
        return comment_to_upvote

    def downvote(self, comment_id):
        """
        @type comment_id: str
        @rtype: comment
        """

        comment_database_worker = CommentdatabaseWorker()
        comment_to_downvote = self.get_comment_by_id(comment_id)
        comment_to_downvote.set_score(comment_database_worker.downvote(comment_id))
        return comment_to_downvote





