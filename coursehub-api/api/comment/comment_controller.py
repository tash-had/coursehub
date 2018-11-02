from api.comment.comment_manager import CommentManager
from flask import jsonify, Blueprint, request

from api.comment.comment import Comment

comment_controller_bp = Blueprint("comment_controller_bp", __name__)


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
        @type course_id: str
        @rtype: JSON[]

        """

        comment_to_post = self.comment_manager.create_comment(course_id, text)
        return jsonify(comment_to_post.__dict__)

    def get_comments_by_course(self, course_id):
        """
        @type course_id: str
        @rtype: JSON[]

        """
        comments = self.comment_manager.get_comments_by_course(course_id)
        comments_dictionary = {"comments": [Comment(comment[4], comment[2], comment[3], comment[1], comment[0]).__dict__ for comment in comments]}
        return jsonify(comments_dictionary)

    def upvote(self, comment_id):
        """
        @type comment_id: str
        @rtype: JSON[]

        """
        comment_to_upvote = self.comment_manager.upvote(comment_id)
        return jsonify(comment_to_upvote.__dict__)

    def downvote(self, comment_id):
        """
        @type comment_id: str
        @rtype: JSON[]
        """

        comment_to_downvote = self.comment_manager.downvote(comment_id)
        return jsonify(comment_to_downvote.__dict__)


comment_controller = CommentController(CommentManager())

@comment_controller_bp.route("/post_comment")

def post_comment():
    text, course_id = request.args.get("comment_text"), request.args.get("course_id")
    comment_controller.post_new_comment(text, course_id)
    comment_controller.post_new_comment(text, course_id)
    comment_controller.upvote(comment_controller.comment_manager.get_comments_by_course(course_id)[0][0])
    comment_controller.upvote(comment_controller.comment_manager.get_comments_by_course(course_id)[0][0])
    comment_controller.upvote(comment_controller.comment_manager.get_comments_by_course(course_id)[0][0])
    comment_controller.downvote(comment_controller.comment_manager.get_comments_by_course(course_id)[0][0])
    comment_controller.downvote(comment_controller.comment_manager.get_comments_by_course(course_id)[1][0])
    comment_controller.downvote(comment_controller.comment_manager.get_comments_by_course(course_id)[1][0])
    comment_controller.downvote(comment_controller.comment_manager.get_comments_by_course(course_id)[1][0])
    comment_controller.upvote(comment_controller.comment_manager.get_comments_by_course(course_id)[1][0])
    return comment_controller.get_comments_by_course(course_id)





