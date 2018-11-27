from api.comment.comment_manager import CommentManager
from flask import jsonify, Blueprint, request
from api.comment.comment import Comment
from api.auth import get_user_with_request

comment_controller_bp = Blueprint("comment_controller_bp", __name__)
comment_manager = CommentManager()


@comment_controller_bp.route("/post_comment", methods=["POST"])
def post_new_comment():
    """
    @rtype: JSON[]

    """
    user = get_user_with_request(request)
    comment_text = request.args.get("commentText")
    course_id = request.args.get("courseId")

    #0 if it has no parent
    parent_id = request.args.get("parentId")

    posted_comment = comment_manager.create_comment(course_id, comment_text, user.id, parent_id)
    return jsonify(posted_comment.__dict__)


@comment_controller_bp.route("/get_comments")
def get_comments_by_course():
    """
    @rtype: JSON[]

    """
    course_id = request.args.get("courseId")

    comments = comment_manager.get_comments_by_course(course_id)
    a = Comment(1, "hi", 17, "courseid", "commentId", )
    b = Comment()
    # Comment(comment[4], comment[2], comment[3], comment[1], comment[0],
    #         comment[7], comment[6], comment[5]).__dict__
    # for comment in
    #     comments]
    #
    comments_dictionary = {
        "comments": [a, b]}

    return jsonify(comments_dictionary)


@comment_controller_bp.route("/upvote", methods=["UPDATE"])
def upvote():
    """
    @rtype: JSON[]

    """
    user = get_user_with_request(request)
    comment_id = request.args.get("commentId")

    comment_to_upvote = comment_manager.upvote(comment_id, user.id)
    return jsonify(comment_to_upvote.__dict__)


@comment_controller_bp.route("/downvote", methods=["UPDATE"])
def downvote():
    """
    @rtype: JSON[]
    """
    user = get_user_with_request(request)
    comment_id = request.args.get("commentId")

    comment_to_downvote = comment_manager.downvote(comment_id, user.id)
    return jsonify(comment_to_downvote.__dict__)



