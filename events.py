from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask import json
from students_model import Students
from blue_print import student_blueprint


My_app = Flask(__name__, instance_relative_config=True)
My_app.register_blueprint(student_blueprint)
student_obj = Students()

#Geta all students
@My_app.route('/api/get-students', methods=['GET'])
def get_all_students():
    " A function to get all students"
    if student_obj.return_student():
        return jsonify(student_obj.return_student()), 200
    else:
        return jsonify ({"Empty student list" : "Please add student"}), 404


@My_app.route("/api/add-student", methods=['POST'])
def add_student():
    "A function to add a student"
    bol = True
    if request.data:
        student_details= request.json
        if student_obj.validate_student_obj(student_details):
            student_name = student_details['student_name']
            student_location = student_details['student_location']
            student_age = student_details['student_age']
            for student in student_obj.student_list:

                if student["student_name"] == student_name:
                    bol = False
                else :
                    bol = True

            if bol:
                student_obj.add_student(student_name, student_pasword, student_location, student_age)
                return jsonify(student_obj.student_list), 201
            else :
                message = {"ERROR": "student name already exists, please try another name"}
                return jsonify(message), 409 
        else :
            return jsonify({"invalid student_object format": "Please Post a valid student object "}),409
    else :
        return jsonify({"Empty student object": "Please Post student details "}), 404
        
@My_app.route("/api/delete/<student_id>", methods=['DELETE'])
def delete_student(student_id):
    "A function to delete a student"
    message = {}
    del_student = {}
    for student in student_obj.students_list:
        if student["student_id"] == str(student_id):
           del_student = student

        else :
            message = {"Error": "Student id dosent exist"}

    if del_student:
         student_obj.delete_student(del_student)
         return jsonify(student_obj.students_list), 200
    else:
         return jsonify(message) ,404



if __name__ == '__main__':
    My_app.run(port=5000, debug=True)