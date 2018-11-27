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

    # 0 if it has no parent
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
    comments_dic = {}

    # put all comments into a dictionary mapping comment id to Comment object
    for comment in comments:
        comments_dic[comment.get_comment_id()] = Comment(comment[4], comment[2], comment[3], comment[1], comment[0],
            comment[7], comment[6], comment[5], get_username_by_id(comment[0]))

    # empty comments and fill it only with root comments
    comments = []
    for comment in comments:
        if comment.is_root():
            comments.append(make_comment_tree(comments_dic, comment))

    dic_to_return = {"comments": [comment.__dict__ for comment in comments]}

    return jsonify(dic_to_return)


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

#comment dic maps comment id's to comment objects
def make_comment_tree(comment_dic, comment):
    comment.set_replies([])
    children = comment_dic[comment.get_comment_id()].get_replies()
    if not children:
        return comment
    else:
        for child in children:
            comment.add_reply(make_comment_tree(comment_dic, child))

        return comment



