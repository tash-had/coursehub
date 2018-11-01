from db.database_manager import DatabaseManager, CourseDatabaseWorker
from .course import Course


class CourseManager:

    db_manager = DatabaseManager()
    course_db_worker = CourseDatabaseWorker()

    @staticmethod
    def build_course_obj(course_row):
        id_ = course_row[0]
        code = course_row[1]
        description = course_row[2]
        title = course_row[3]
        org_name = course_row[4]
        # w_rating = course_row[5]
        # r_rating = course_row[6]
        # overall_rating = course_row[7]
        # rating_count = course_row[8]

        # ratings = {"workload": w_rating, "recommendation": r_rating}

        return Course(code, id_, description, title, org_name)

    @staticmethod
    def get_course_rating_names():
        return ["workload", "recommendation"]

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

        if len(course_info) != 1:
            raise Exception("invalid ID")

        return CourseManager.build_course_obj(course_info[0])

    @staticmethod
    def update_course_rating(course, new_ratings):
        """
        :param course: Course obj
        :param new_ratings: (dict) newly added ratings
        :return:
        """
        overall_rating = course.get_overall_rating()
        count = course.get_rating_count()
        rating_sum = 0

        for r_type in new_ratings:
            prev_rating = course.get_ratings()[r_type]
            rating_sum += new_ratings[r_type]

            updated_rating = CourseManager.calculate_course_rating(prev_rating, count, new_ratings[r_type])
            CourseManager.course_db_worker.update_course_field(course.get_id(), r_type, updated_rating)

        rating_average = rating_sum / len(new_ratings)
        updated_overall_rating = CourseManager.calculate_course_rating(overall_rating, count, rating_average)
        CourseManager.course_db_worker.update_course_field(course.get_id(), "overall_rating", updated_overall_rating)

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
