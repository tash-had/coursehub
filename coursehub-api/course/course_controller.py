from flask import Flask, jsonify, abort, request

app = Flask(__name__)
URL_PREFIX = "/api/v1.0"


# endpoint goes here
def search_for_course():
    """
    :return: array of JSON dict of all matching courses
    """
    course_code = request.args.get("courseCode")

    courses = CourseManager.get_courses_by_code(course_code)

    return jsonify([course.__dict__ for course in courses])


# endpoint goes here
def select_course():
    """
    :return: course by ID
    """
    return jsonify(CourseManager.get_course_by_id(request.args.get("ID")).__dict__)


# endpoint goes here
def update_rating():
    """
    :return: course object with updated rating
    """
    workload = request.args.get("workload")  # must be either 'workload' or 'recommendation'
    recommendation = request.args.get("recommendation")
    course_id = request.args.get("ID")

    rating_dict = {"workload": workload, "recommendation": recommendation}

    course = CourseManager.get_course_by_id(course_id)

    new_course = CourseManager.update_course_rating(course, rating_dict)

    return jsonify(new_course.__dict__)
