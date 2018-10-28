from flask import Flask, jsonify, abort, request
from managers.course_manager import CourseManager

app = Flask(__name__)
URL_PREFIX = "/api/v1.0"


def select_course(course_code):
    """
    :param course_code: the str entered by user's search
    :return: JSON dict of all matching courses
    """
    course = CourseManager.get_course_by_code(course_code)

    return jsonify({"code": course.get_code(),
                    "id": course.get_id(),
                    "description": course.get_description(),
                    "rating": course.get_rating()})
