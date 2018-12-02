from flask import Blueprint, jsonify, request
from api.user.user_manager import UserManager
from api.auth import get_user_with_request

user_controller_bp = Blueprint("user_controller", __name__)


@user_controller_bp.route("/view_user_profile")
def view_user_profile():
    """
    :return: array of JSON dict of the user's info
    """
    user = get_user_with_request(request)
    user.comment_history = UserManager.get_comments_by_user_id(user.id)
    resp = user.__dict__
    resp["comment_history"] = {
        "comments": user.comment_history,
        "num_comments": len(user.comment_history)
    }
    return jsonify(resp)


@user_controller_bp.route("/sign_in", methods=["POST"])
def sign_in():
    """
    if this is their first time signing in, add them to DB
    """
    auth_token_arg = request.get_json()["idToken"]
    auth_param = auth_token_arg if auth_token_arg else request
    user = get_user_with_request(auth_param)
    if not UserManager.is_user_in_db(user.id):
        UserManager.add_new_user(user)

    return jsonify(user.__dict__)
