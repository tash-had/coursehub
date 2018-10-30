from flask import Flask, jsonify, abort, request
from managers.course_manager import CourseManager

app = Flask(__name__)
URL_PREFIX = "/api/v1.0"


# endpoint goes here
def select_course(course_code):
    """
    :param course_code: the str entered by user's search
    :return: array of JSON dict of all matching courses
    """
    courses = CourseManager.get_courses_by_code(course_code)

    return jsonify([course.__dict__ for course in courses])
