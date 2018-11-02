from flask import Flask, abort, jsonify, request
from api.course.course_controller import course_controller_bp
from api.comment.comment_controller import comment_controller_bp
from flask_cors import CORS, cross_origin


URL_PREFIX = "/api/v1.0"

app = Flask(__name__)
app.register_blueprint(course_controller_bp, url_prefix=URL_PREFIX + "/course")
app.register_blueprint(comment_controller_bp, url_prefix=URL_PREFIX + "/comment")

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    abort(403)

if __name__ == '__main__':
    app.run(debug=True)
