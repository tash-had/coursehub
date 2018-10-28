import datetime


class Comment:
    """
    An object that is a comment on a Course.

    Attributes:
    ===========
    @type score: int
    @type text: str
    @type time_stamp: datetime.datetime
    @type courseID: int
    @type ID: int
    @rtype: None

    """

    def __init__(self, score, text, time_stamp, course_id, comment_id):
        """
        @type score: int
        @type text: str
        @type time_stamp: datetime.datetime
        @type course_id: int
        @type comment_id: int
        @rtype: None

        """
        self.score = score
        self.text = text
        self.time_stamp = time_stamp
        self.course_id = course_id
        self.comment_id = comment_id

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_time_stamp(self):
        return self.time_stamp

    def get_course(self):
        pass

    def set_course(self, course):
        pass

    def get_text(self):
        return self.text

    def get_course_id(self):
        return self.course_id

    def get_comment_id(self):
        return self.comment_id






