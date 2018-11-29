from api.comment.comment import Comment


def build_comment(comment):
    return Comment(comment[4], comment[2], comment[3], comment[1], comment[0])
