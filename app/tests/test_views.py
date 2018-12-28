from django.test import TestCase, Client

from app.models.course import Course
from app.models.student import Student
import datetime

from django.contrib.auth.models import User
from app.models.course import Course
from app.models.student import Student
from app.serializers.course_serializer import CourseSerializer
from app.serializers.student_serializer import StudentSerializer

class GetAllCoursesTest(TestCase):
    """ Test module for GET all courses API """
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        print(datetime.datetime.now())
        Course.objects.create(
            code='test-code-213',
            name="This is test course",
            starting_date=datetime.datetime.now(),
            ending_date=datetime.datetime.now() + datetime.timedelta(days=1))
        User.objects.create_user(
            username='test', email='foo@bar.com', password='top_secret')

    def test_get_all_courses(self):
        # get API response
        c = Client()
        logged_in = c.post(
            '/api/login/', {'username': 'test', 'password': 'top_secret'})

        response = c.get('/api/courses/')
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        print(response)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_only_login_user_can_access_the_courses_endpoint(self):
            print("Method: test_only_login_user_can_access_the_courses_endpoint.")
            c = Client()
            print(User.email)
            logged_in = c.post(
                '/api/login/', {'username': 'test', 'password': 'top_secret'})

            response = c.get('/api/courses/')
            print(response)

            self.assertEqual(response.status_code, 200)


class GetAllStudentsTest(TestCase):
    """ Test module for GET all Students API """
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        print(datetime.datetime.now())
        user = User.objects.create_user(
            username='test', email='foo@bar.com', password='top_secret', first_name='Foo', last_name='bar')

        courses = Course.objects.bulk_create([
            Course(code='test-code-213',
                   name="This is test course",
                   starting_date=datetime.datetime.now(),
                   ending_date=datetime.datetime.now() + datetime.timedelta(days=1), created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()),
            Course(code='test-code-456',
                   name="This is test course - 2",
                   starting_date=datetime.datetime.now(),
                   ending_date=datetime.datetime.now() + datetime.timedelta(days=30), created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()),
        ])

        Student.objects.create(
            user=user,
            dob='1980-1-1',
            gender='F',
            active=True
        )
        Student.courses = courses

    def test_get_all_students(self):
        # get API response
        c = Client()
        logged_in = c.post(
            '/api/login/', {'username': 'test', 'password': 'top_secret'})

        response = c.get('/api/students/')
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        print(response)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_only_login_user_can_access_the_students_endpoint(self):
        print("Method: test_only_login_user_can_access_the_students_endpoint.")
        c = Client()
        logged_in = c.post(
            '/api/login/', {'username': 'test', 'password': 'top_secret'})

        response = c.get('/api/students/')
        print(response)

        self.assertEqual(response.status_code, 200)
