from flask import  Blueprint
from flask import jsonify

student_blueprint = Blueprint('student_blue', __name__ )

@student_blueprint.route('/blue', methods = ["GET"])
def index():
    "An example of a blue print"
    return jsonify({"message": "This is a blue print"})