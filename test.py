import unittest
import json
from students_model import Students
from events import My_app

class Test_Case(unittest.TestCase):

    def setUp(self):
        " setting p variables to run before test"
        self.user_obj = Students()
        self.hostname = "http://localhost:5000/api/"
        self.app = My_app.test_client()
        self.app.testing = True
        self.student = {
	             "student_name" : "NAKAWEESI",
                 "student_pasword" : "jovia",
                 "student_location": "makindye",
                 "student_age" :22
                    }


    def test_wrong_get_method(self):
        "asserting a wrong method for get"
        res = self.app.post(self.hostname + "get-student", data=self.student)
        self.assertEqual(res.status_code, 405)

    def test_right_get_method(self):
        "asserting a correct method"
        res = self.app.get(self.hostname + "get-students")
        self.assertEqual(res.status_code, 200)

    def test_wrong_post_method(self):
        " asserting a wrong method foor post"
        resp = self.app.get(self.hostname + "add-student", data=self.student)
        self.assertEquals(resp.status_code, 405)

    def test_rigt_method(self):
        "asserting a right method for post"
        resp = self.app.post(self.hostname + "add-student", data=self.student)
        self.assertEquals (resp.status_code ,200)

    def test_wrong_delete_method(self):
        "asserting a wrong delete method"
        res = self.app.post(self.hostname + "delete/dd", data=self.student)
        self.assertEqual(res.status_code, 405)

    def test_right_delete_method(self):
        "asserting a correct delete method"
        res = self.app.delete(self.hostname + "delete/dd")
        self.assertEqual(res.status_code, 200)

    def test_empty_user_list(self):
        "asserting student list is empty before any post"
        resp = self.app.get(self.hostname + "get-students")
        self.assertEqual(len(self.student_obj.students_list), 0)

    def test__student_added_to_list(self):
        "asserting a student added after a correct pst method"
        resp = self.app.post(self.hostname + "add-student", data = json.dumps(self.student ),content_type='application/json',)
        #resp = self.app.get(self.hostname + "get-student")
        self.assertIn(self.student['student_name'], str(resp.data))