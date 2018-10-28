from Comment import Comment
import datetime


class CommentManager:
    """
    Attributes:
    ===========
    @type comments: Comment[]
    @rtype: None

    """

    def __init__(self, comments):
        """

        @type comments: Comment[]
        @rtype: None

        """

        self.comments = comments

    def create_comment(self, course_id, time_stamp, text):
        """

        @type course_id: int
        @type time_stamp: datetime.datetime
        @type text: str
        @rtype: None
        """
        pass

    def get_comments_by_course(self, course_id):
        """

        @type course_id: int
        @rtype: Comment[]
        """
        pass

    def get_comment_by_id(self, comment_id):
        """

        @type comment_id: int
        @rtype: Comment
        """
        pass



