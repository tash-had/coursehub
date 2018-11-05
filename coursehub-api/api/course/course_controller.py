from flask import Blueprint, jsonify, request
from api.course.course_manager import CourseManager

course_controller_bp = Blueprint("course_controller", __name__)


@course_controller_bp.route("/search_course")
def search_for_course():
    """
    :return: array of JSON dict of all matching courses
    """
    course_code = request.args.get("searchQuery")

    if course_code == "":
        return jsonify({"error": "No matching courses found for '" + course_code + "'"})

    courses = CourseManager.get_courses_by_code(course_code)

    if courses is None:
        return jsonify({"error": "No matching courses found for '" + course_code + "'"})

    return jsonify({"matching_courses": courses})


@course_controller_bp.route("/get_course_data")
def get_course_data():
    """
    :return: course by ID
    """
    id_ = request.args.get("courseId")

    return jsonify(CourseManager.get_course_by_id(id_).__dict__)


@course_controller_bp.route("/add_course_ratings")
def update_rating():
    """
    :return: course object with updated rating
    """
    workload = request.args.get("workloadRating")  # must be either 'workload' or 'recommendation'
    recommendation = request.args.get("recommendationRating")
    course_id = request.args.get("courseId")

    rating_dict = {"workload_rating": workload, "recommendation_rating": recommendation}

    course = CourseManager.get_course_by_id(course_id)

    new_course = CourseManager.update_course_rating(course, rating_dict)

    ratings = {}
    ratings["overall_rating"] = new_course.overall_rating
    ratings["workload_rating"] = new_course.ratings["workload_rating"]
    ratings["recommendation_rating"] = new_course.ratings["recommendation_rating"]

    return jsonify(ratings)
