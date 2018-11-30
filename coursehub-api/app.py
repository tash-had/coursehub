import os

from flask import Flask, abort
from api.course.course_controller import course_controller_bp
from api.comment.comment_controller import comment_controller_bp
from api.user.user_controller import user_controller_bp
from flask_cors import CORS


URL_PREFIX = "/api/v1.0"

app = Flask(__name__)
app.register_blueprint(course_controller_bp, url_prefix=URL_PREFIX + "/course")
app.register_blueprint(comment_controller_bp, url_prefix=URL_PREFIX + "/comment")
app.register_blueprint(user_controller_bp, url_prefix=URL_PREFIX + "/user")

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    abort(403)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)