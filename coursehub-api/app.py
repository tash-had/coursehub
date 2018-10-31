from flask import Flask, jsonify, abort, request
from db.database_manager import DatabaseManager
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

URL_PREFIX = "/api/v1.0"


@app.route('/')
def home():
    abort(403)


@app.route(URL_PREFIX + '/hello')
def test_endpoint():
    return jsonify({"msg":"hello world",
                    "data": [1, 2, 3, 4, 5, 6]})



@app.route(URL_PREFIX + '/login')
def not_so_secure_login():
    """ Login a user 
    Request parameters: email, password 

    :return dict: the given credentials
    """
    username, password = request.json.get("email"), request.json.get("password")
    return jsonify({"username": username,
                    "password": password})

# @TODO
"""REMOVE THIS BEFORE PUSHING TO MASTER"""
@app.route(URL_PREFIX + '/course_data')
@cross_origin()
def get_course_data_with_course_code():

    course_code = request.args.get("courseCode")
    dm = DatabaseManager()
    course_data = dm.get_course_data(course_code)
    return jsonify({"courseData": {
        "courseId": course_data[0][0],
        "courseCode": course_data[0][1],
        "courseDescription": course_data[0][2],
        "courseName": course_data[0][3],
        "courseOrg": course_data[0][4]

    }})

@app.route(URL_PREFIX + '/search_course')
@cross_origin()
def search_course():

    course_code = request.args.get("searchQuery")

    dm = DatabaseManager()

    c1 = ["CSC165H1", "CSC148H1", "CSC108H1"]
    c2 = ["CSC258H1", "CSC236H1"]
    c3 = ["CSC301H1"]
    c = []
    if course_code == "CSC1":
        c = c1
    elif course_code == "CSC16":
        c = c2
    elif course_code == "CSC165":
        c = c3
    res = []
    for i in c:
        course_data = dm.get_course_data(i)
        d = {
            "courseId": course_data[0][0],
            "courseCode": course_data[0][1],
            "courseDescription": course_data[0][2],
            "courseName": course_data[0][3],
            "courseOrg": course_data[0][4]

        }
        res.append(d)
    return jsonify({"matchingCourses": res})



if __name__ == '__main__':
    app.run(debug=True)
