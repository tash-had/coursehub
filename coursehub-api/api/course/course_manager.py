from api.course.course import Course
from db.workers.course_database_worker import CourseDatabaseWorker


class CourseManager:

    course_db_worker = CourseDatabaseWorker()

    @staticmethod
    def build_course_obj(course_row):
        id_ = course_row[0]
        code = course_row[1]
        description = course_row[2]
        title = course_row[3]
        org_name = course_row[4]
        w_rating = course_row[5]
        r_rating = course_row[6]
        overall_rating = course_row[7]
        rating_count = course_row[8]

        ratings = {"workload_rating": w_rating, "recommendation_rating": r_rating}

        return Course(code, id_, description, title, org_name, ratings, overall_rating, rating_count)

    @staticmethod
    def get_course_rating_names():
        return ["workload_rating", "recommendation_rating"]

    @staticmethod
    def get_courses_by_code(course_code):
        """
        :param course_code: str
        :return: Course[]
        """

        courses_info = CourseManager.course_db_worker.get_courses_data(course_code)

        if len(courses_info) == 0:
            return None

        return [CourseManager.build_course_obj(course_info).__dict__ for course_info in courses_info]

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
    def update_course_rating(course, new_ratings, remove_or_add):
        """
        :param course: Course obj
        :param new_ratings: (dict) newly added ratings
        :param remove_or_add: str - "remove" or "add"
        :return:
        """
        overall_rating = course.get_overall_rating()
        count = course.get_rating_count()
        rating_sum = 0

        for r_type in new_ratings:
            prev_rating = course.get_ratings()[r_type]
            rating_sum += int(new_ratings[r_type])

            updated_rating = CourseManager.calculate_course_rating(prev_rating, count,
                                                                   int(new_ratings[r_type]), remove_or_add)
            CourseManager.course_db_worker.update_course_field(course.get_id(), r_type, updated_rating)

        rating_average = rating_sum / len(new_ratings)

        updated_overall_rating = CourseManager.calculate_course_rating(overall_rating, count,
                                                                       rating_average, remove_or_add)
        CourseManager.course_db_worker.update_course_field(course.get_id(), "overall_rating", updated_overall_rating)

        if remove_or_add == 'remove':
            new_rating_count = course.rating_count - 1
        else:
            new_rating_count = course.rating_count + 1
        CourseManager.course_db_worker.update_course_field(course.get_id(), "num_ratings", new_rating_count)

        new_course = CourseManager.course_db_worker.get_course_by_id(course.get_id())

        return CourseManager.build_course_obj(new_course[0])

    @staticmethod
    def calculate_course_rating(old_rating, rating_count, new_rating, remove_or_add):
        """
        :param old_rating: prev rating(float)
        :param rating_count: # of ratings in prev rating(int)
        :param new_rating: int
        :param remove_or_add: str ("remove" or "add")
        :return: aggregated rating (float)
        """
        if remove_or_add == 'remove':
            return (old_rating * rating_count - new_rating) / (rating_count - 1)
        else:
            return (old_rating * rating_count + new_rating) / (rating_count + 1)

    @staticmethod
    def did_user_already_rate_course(user_id, course):
        """
        param user_id: str
        param course: Course
        """

        # if there exists an entry in user-course-ratings table
        # with the given course and id, return True

        return True

    @staticmethod
    def get_prev_ratings(user_id, course, ratings):
        """
        param user_id: str
        param course: Course
        """

        for rating_type in ratings:
            ratings[rating_type] = None  # DB.user_course_ratings.get[rating_type]where[user_id]=user_id

        return ratings

    @staticmethod
    def update_user_course_ratings(user_id, course, ratings):
        """
        :param user_id: str
        :param course: Course
        :param ratings: dict[rating type (str): int]
        """
        for rating_type, rating in ratings:
            pass  # DB.user_course_ratings.where[user_id]=user_id.update[rating_type]=rating
