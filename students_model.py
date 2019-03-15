import uuid
class Students :
    "Model class for students"

    def __init__(self):
        "Decalring class member"
        self.student_details = {}
        self.student_id = ""
        self.student_name = ""
        self.student_location = ""
        self.student_age=  ""

    def add_student(self,student_name, student_id, student_location, student_age):
        "A function to add a student"
        self.student_id = str(uuid.uuid1())
        self.student_name = student_name
        self.id_student = user_id
        self.student_location =student_location
        self.student_age= student_age
        self.student_details = {
                "student_id" : self.student_id ,
                "student_name" : self.student_name,
                "student_location": self.student_location,
                 "student_age" : self.student_age
                 }
        self.students_list.append(self.student_details )




    def validate_student_obj (self, student_Obj):
        "A function to validate a student object"
        if ("student_name" in user_Obj and "student_pasword" in user_Obj
            and "student_location" in user_Obj and "student_age" in user_Obj):
            return True
        else:
            return False


    def return_student (self):
        "a Function to return all student"
        return self.students_list

    def delete_student(self, student):
        "A function to delete a student from the List"
        self.student_list.remove(student)
