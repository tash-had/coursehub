from db.workers.user_database_worker import UserDatabaseWorker
from db.workers.comment_database_worker import CommentDatabaseWorker
from api.comment.comment_factory import build_comment


class UserManager:

    user_db_worker = UserDatabaseWorker()
    comment_db_worker = CommentDatabaseWorker()

    @staticmethod
    def user_id_to_username(user_id):
        return UserManager.user_db_worker.get_username_by_id(user_id)

    @staticmethod
    def get_comments_by_user_id(user_id):
        comments = UserManager.comment_db_worker.get_comments_by_user_id(user_id)
        comment_lst = []
        for comment in comments:
            comment_lst.append(build_comment(comment).__dict__)

        return comment_lst

    @staticmethod
    def is_user_in_db(user_id):
        return len(UserManager.user_db_worker.get_username_by_id(user_id)) > 0

    @staticmethod
    def add_new_user(user):
        UserManager.user_db_worker.add_new_user(user)
