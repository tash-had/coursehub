from db.database_manager import DatabaseManager, CourseDatabaseWorker
from objects.course import Course


class CourseManager:

    db_manager = DatabaseManager()
    course_db_worker = CourseDatabaseWorker()

    @staticmethod
    def get_course_by_code(course_code):
        """
        :param course_code: str
        :return: Course
        """

        course_info = CourseManager.course_db_worker.get_course_data(course_code)

        code = course_info["code"]
        id_ = course_info["id"]
        description = course_info["description"]
        rating = course_info["rating"]

        return Course(code, id_, description, rating)
