import time
import uuid

from api.comment.comment import Comment
from db.workers.comment_database_worker import CommentDatabaseWorker
from db.workers.user_to_comment_database_worker import UserToCommentDatabaseWorker
from db.workers.user_database_worker import UserDatabaseWorker

comment_database_worker = CommentDatabaseWorker()
user_to_comment_database_worker = UserToCommentDatabaseWorker()


class CommentManager:
    def __init__(self):
        self.user_database_worker = UserDatabaseWorker()

    def create_comment(self, course_id, text, user_id, parent_id):
        """

        @type course_id: str
        @type text: str
        @type user_id: str
        @type parent_id: str
        @rtype: comment
        """
        comment_id = str(uuid.uuid4())
        time_stamp = time.time()

        user_to_comment_database_worker.insert_row(user_id, comment_id)
        user_to_comment_database_worker.set_rating(user_id, comment_id, "upvote")

        is_root = 1
        if parent_id is not None:
            is_root = 0
            comment_database_worker.add_children_to_comment(parent_id,
                                                            comment_id)

        data = {"id": comment_id, "course_id": course_id, "comment": text,
                "timestamp": time_stamp, "votes": 1, "user_id": user_id,
                "children": "", "root": is_root}

        comment_database_worker.insert_comment(data)

        return Comment(1, text, time_stamp, course_id, comment_id, user_id, [],
                       is_root,
                       self.user_database_worker.get_username_by_id(comment_id))

    def get_comments_by_course(self, course_id):
        """

        @type course_id: str
        @rtype: comment[]
        """
        return comment_database_worker.get_comments_for_course(course_id)

    def get_comment_by_id(self, comment_id):
        """

        @type comment_id: str
        @rtype: comment
        """
        result = comment_database_worker.get_comment_by_id(comment_id)
        return Comment(result[4], result[2], result[3], result[1], result[0],
                       result[7], result[6], result[5], self.user_database_worker.get_username_by_id(result[7])[0][0])

    def upvote(self, comment_id, user_id):
        """
        @type comment_id: str
        @type user_id: int
        @rtype: comment

        """
        user_to_comment_database_worker.insert_row(user_id, comment_id)
        comment_to_upvote = self.get_comment_by_id(comment_id)
        if user_to_comment_database_worker.get_rating(user_id, comment_id) == "upvote":
            user_to_comment_database_worker.set_rating(user_id, comment_id, "None")
            comment_to_upvote.set_score(comment_database_worker.downvote(comment_id))

        elif user_to_comment_database_worker.get_rating(user_id, comment_id) == "None":
            user_to_comment_database_worker.set_rating(user_id, comment_id, "upvote")
            comment_to_upvote.set_score(comment_database_worker.upvote(comment_id))

        elif user_to_comment_database_worker.get_rating(user_id, comment_id) == "downvote":
            user_to_comment_database_worker.set_rating(user_id, comment_id, "upvote")
            comment_to_upvote.set_score(comment_database_worker.upvote(comment_id))
            comment_to_upvote.set_score(comment_database_worker.upvote(comment_id))

        return comment_to_upvote

    def downvote(self, comment_id, user_id):
        """
        @type comment_id: str
        @type user_id: int
        @rtype: comment
        """

        user_to_comment_database_worker.insert_row(user_id, comment_id)
        comment_to_upvote = self.get_comment_by_id(comment_id)
        if user_to_comment_database_worker.get_rating(user_id, comment_id) == "upvote":
            user_to_comment_database_worker.set_rating(user_id, comment_id, "downvote")
            comment_to_upvote.set_score(comment_database_worker.downvote(comment_id))
            comment_to_upvote.set_score(comment_database_worker.downvote(comment_id))

        elif user_to_comment_database_worker.get_rating(user_id, comment_id) == "None":
            user_to_comment_database_worker.set_rating(user_id, comment_id, "downvote")
            comment_to_upvote.set_score(comment_database_worker.downvote(comment_id))

        elif user_to_comment_database_worker.get_rating(user_id, comment_id) == "downvote":
            user_to_comment_database_worker.set_rating(user_id, comment_id, "None")
            comment_to_upvote.set_score(comment_database_worker.upvote(comment_id))

        return comment_to_upvote




