from db.database_manager import DatabaseManager, CourseDatabaseWorker
from objects.course import Course


class CourseManager:

    db_manager = DatabaseManager()
    course_db_worker = CourseDatabaseWorker()

    @staticmethod
    def build_course_obj(course_row):
        code = course_row["code"]
        id_ = course_row["id"]
        description = course_row["description"]
        rating = course_row["rating"]

        return Course(code, id_, description, rating)

    @staticmethod
    def get_course_by_code(course_code):
        """
        :param course_code: str
        :return: Course
        """

        course_info = CourseManager.course_db_worker.get_course_data(course_code)

        return CourseManager.build_course_obj(course_info)

    @staticmethod
    def get_course_by_id(id_):
        """
        :param id_: int
        :return: Course
        """

        course_info = CourseManager.course_db_worker.get_course_by_id(id_)

        return CourseManager.build_course_obj(course_info)

