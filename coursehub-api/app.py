from flask import Flask, jsonify, abort, request

app = Flask(__name__)
URL_PREFIX = "/api/v1.0"

from course.course_controller import course_controller_bp
app.register_blueprint(course_controller_bp, url_prefix=URL_PREFIX)


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

if __name__ == '__main__':
    app.run(debug=True)
