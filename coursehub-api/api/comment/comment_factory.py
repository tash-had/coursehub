from api.comment.comment import Comment
from db.workers.user_database_worker import UserDatabaseWorker

user_database_worker = UserDatabaseWorker()


def build_comment(comment):
    return Comment(comment[4], comment[2], comment[3], comment[1], comment[0],
                   comment[7], comment[6], comment[5],
                   user_database_worker.get_username_by_id(comment[7])[0][0])
