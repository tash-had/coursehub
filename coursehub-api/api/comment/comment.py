
class Comment:
    """
    An object that is a comment on a Course.

    Attributes:
    ===========
    @type score: int
    @type text: str
    @type time_stamp: int
    @type course_id: int
    @type comment_id: str
    @type user_id: int
    @type replies: [int]
    @rtype: None

    """

    def __init__(self, score, text, time_stamp, course_id, comment_id, user_id, replies, root, username):
        """
        @type score: int
        @type text: str
        @type time_stamp: int
        @type course_id: str
        @type comment_id: str
        @type user_id: str
        @type replies: [Comment]
        @type root: bool
        @type username: str
        @rtype: None

        """
        self.score = score
        self.text = text
        self.time_stamp = time_stamp
        self.course_id = course_id
        self.comment_id = comment_id
        self.user_id = user_id
        self.replies = replies
        self.root = root
        self.username = username

    def get_username(self):
        return self.username

    def is_root(self):
        return self.root


    def get_replies(self):
        return self.replies

    def add_reply(self, comment_id):
        self.replies.append(int)

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id


    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_time_stamp(self):
        return self.time_stamp

    def get_text(self):
        return self.text

    def get_course_id(self):
        return self.course_id

    def get_comment_id(self):
        return self.comment_id

    def set_replies(self, replies):
        self.replies = replies





