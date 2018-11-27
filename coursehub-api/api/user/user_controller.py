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

    profile_dict = dict()
    profile_dict["username"] = user.username
    profile_dict["comment_history"] = UserManager.get_comments_by_user_id(user.id)

    return jsonify(profile_dict)


@user_controller_bp.route("/sign_in")
def sign_in():
    """
    if this is their first time signing in, add them to DB
    """
    user = get_user_with_request(request)

    if not UserManager.is_user_in_db(user.id):
        UserManager.add_new_user(user)
