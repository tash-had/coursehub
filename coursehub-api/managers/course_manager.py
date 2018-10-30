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
        u_rating = course_row["usefulness"]
        d_rating = course_row["difficulty"]
        u_rating_count = course_row["u_rating_count"]
        d_rating_count = course_row["d_rating_count"]

        return Course(code, id_, description, u_rating, d_rating, u_rating_count, d_rating_count)

    @staticmethod
    def get_courses_by_code(course_code):
        """
        :param course_code: str
        :return: Course[]
        """

        courses_info = CourseManager.course_db_worker.get_courses_data(course_code)

        return [CourseManager.build_course_obj(course_info) for course_info in courses_info]

    @staticmethod
    def get_course_by_id(id_):
        """
        :param id_: int
        :return: Course
        """

        course_info = CourseManager.course_db_worker.get_course_by_id(id_)

        return CourseManager.build_course_obj(course_info)

    @staticmethod
    def update_course_rating(course, rating_type, new_rating):
        """
        :param course: Course obj
        :param rating_type: (str) usefulness or difficulty
        :param new_rating: (int) newly added rating
        :return:
        """
        if rating_type == 'usefulness':
            rating = course.get_usefulness_rating()
            count = course.get_u_rating_count()
        elif rating_type == 'difficulty':
            rating = course.get_difficulty_rating()
            count = course.get_d_rating_count()
        else:
            return 0

        updated_rating = CourseManager.calculate_course_rating(rating, count, new_rating)

        CourseManager.course_db_worker.update_course_field(course.get_id(), rating_type, updated_rating)

        new_course = CourseManager.course_db_worker.get_course_by_id(course.get_id())

        return CourseManager.build_course_obj(new_course)

    @staticmethod
    def calculate_course_rating(old_rating, rating_count, new_rating):
        """
        :param old_rating: prev rating(float)
        :param rating_count: # of ratings in prev rating(int)
        :param new_rating: int
        :return: aggregated rating (float)
        """
        return (old_rating * rating_count + new_rating)/(rating_count + 1)
