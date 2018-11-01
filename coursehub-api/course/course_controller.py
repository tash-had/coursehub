from flask import Blueprint, jsonify, request
from .course_manager import CourseManager

course_controller_bp = Blueprint("course_controller", __name__)


@course_controller_bp.route("search_course")
def search_for_course():
    """
    :return: array of JSON dict of all matching courses
    """
    course_code = request.args.get("searchQuery")

    courses = CourseManager.get_courses_by_code(course_code)

    if courses is None or course_code == "":
        return jsonify({"error": "No matching courses found for '" + course_code + "'"})

    return jsonify([course.__dict__ for course in courses])


@course_controller_bp.route("select_course")
def select_course():
    """
    :return: course by ID
    """
    id_ = request.args.get("id")

    return jsonify(CourseManager.get_course_by_id(id_).__dict__)


@course_controller_bp.route("add_course_ratings")
def update_rating():
    """
    :return: course object with updated rating
    """
    workload = request.args.get("workload_rating")  # must be either 'workload' or 'recommendation'
    recommendation = request.args.get("recommendation_rating")
    course_id = request.args.get("id")

    rating_dict = {"workload_rating": workload, "recommendation_rating": recommendation}

    course = CourseManager.get_course_by_id(course_id)

    new_course = CourseManager.update_course_rating(course, rating_dict)

    return jsonify(new_course.__dict__)
