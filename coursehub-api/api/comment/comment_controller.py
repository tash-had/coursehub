from api.comment.comment_manager import CommentManager
from flask import jsonify, Blueprint, request
from api.comment.comment import Comment
from api.auth import get_user_with_request
from db.workers.user_database_worker import UserDatabaseWorker

comment_controller_bp = Blueprint("comment_controller_bp", __name__)
comment_manager = CommentManager()
user_database_worker = UserDatabaseWorker()

@comment_controller_bp.route("/post_comment", methods=["POST"])
def post_new_comment():
    """
    @rtype: JSON[]

    """
    user = get_user_with_request(request)
    comment_text = request.args.get("comment_text")
    course_id = request.args.get("course_id")

    parent_id = request.args.get("parent_id")

    comment_manager.create_comment(course_id, comment_text, user.id, parent_id)
    return jsonify(get_comments_helper(course_id))


@comment_controller_bp.route("/delete_comment", methods=["DELETE"])
def delete_comment():
    """

    """
    user = get_user_with_request(request)
    comment_id = request.args.get("commentId")
    if comment_manager.get_comment_by_id(comment_id).user_id == user.id:
        return comment_manager.delete_comment(comment_id)

    return {"error": "denied access to delete comment"}


@comment_controller_bp.route("/get_comments")
def get_comments_by_course():
    """
    @rtype: JSON[]

    """
    course_id = request.args.get("course_id")
    return jsonify(get_comments_helper(course_id))


@comment_controller_bp.route("/upvote", methods=["UPDATE"])
def upvote():
    """
    @rtype: JSON[]

    """
    user = get_user_with_request(request)
    comment_id = request.args.get("comment_id")

    comment_to_upvote = comment_manager.upvote(comment_id, user.id)
    return jsonify(comment_to_upvote.__dict__)


@comment_controller_bp.route("/downvote", methods=["UPDATE"])
def downvote():
    """
    @rtype: JSON[]
    """
    user = get_user_with_request(request)
    comment_id = request.args.get("comment_id")

    comment_to_downvote = comment_manager.downvote(comment_id, user.id)
    return jsonify(comment_to_downvote.__dict__)


def get_comments_helper(course_id):
    """

    :param course_id:
    :type course_id: str
    :return:
    :rtype: dict
    """
    comments = comment_manager.get_comments_by_course(course_id)
    comments_dic = {}

    # put all comments into a dictionary mapping comment id to Comment object
    for comment in comments:
        if comment[6] == "":
            replies = []
        else:
            # first element is "" so we need to skip it
            replies = []
            for comment_id in comment[6].split(" ")[1:]:
                replies.append(comment_manager.get_comment_by_id(comment_id))

        comments_dic[comment[0]] = Comment(comment[4], comment[2], comment[3], comment[1], comment[0],
            comment[7], replies, comment[5], user_database_worker.get_username_by_id(comment[7])[0][0])

    # empty comments and fill it only with root comments
    comments = []
    for comment_id, comment in comments_dic.items():
        if comment.is_root():
            comments.append(make_comment_tree(comments_dic, comment))

    return {"comments": [dictionarify_comment_tree(comment) for comment in comments]}

def make_comment_tree(comment_dic, comment):
    """
    Comment_dic maps comment id's to comment objects.  Set replies of comment to be full comment tree instead of just first level.

    :param comment_dic:
    :type comment_dic:
    :param comment:
    :type comment:
    :return:
    :rtype:
    """
    replies = []
    children = comment_dic.get(comment.get_comment_id()).get_replies()
    if not children:
        # replies to comment was ""
        comment.set_replies([])
        return comment
    else:
        for child in children:
            replies.append(make_comment_tree(comment_dic, child))

        comment.set_replies(replies)

        return comment


def dictionarify_comment_tree(comment):
    """

    :param comment:
    :type comment: Comment
    :return:
    :rtype: dict
    """
    if comment.get_replies == []:
        return comment.__dict__
    else:
        comment.set_replies([dictionarify_comment_tree(reply) for reply in comment.get_replies()])
        return comment.__dict__
