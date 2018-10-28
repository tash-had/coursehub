from comment import Comment
from flask import jsonify
from db.database_manager import c


class CommentController:
    """
    Attributes:
    ===========
    @type comment_manager: CommentManager
    @rtype: None

    """

    def __init__(self, comment_manager):
        """

        @type comment_manager: CommentManager
        @rtype: None

        """

        self.comment_manager = comment_manager

    def post_new_comment(self, text, course_id):
        """

        @type text: str
        @type course_id: int
        @rtype: JSON[]

        """

        comment = self.comment_manager.create_comment(course_id, text)
        return jsonify({"id": comment.get_comment_id(),
                 "course_id": comment.get_course_id(),
                 "comment": comment.get_text(),
                 "time": comment.get_time_stamp(),
                 "votes": comment.get_score()})

    def get_comments_by_course(self, course_id):
        """
        @type course_id: int
        @rtype: JSON[]

        """
        comments = self.comment_manager.get_comments_by_course(course_id)
        return jsonify({"comments": comments})

    def upvote(self, comment_id):
        """
        @type comment_id: int
        @rtype: JSON[]

        """

        pass

    def downvote(self, comment_id):
        """
        @type comment_id: int
        @rtype: JSON[]
        """

        pass

