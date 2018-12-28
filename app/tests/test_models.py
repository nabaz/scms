from django.test import TestCase, Client

from app.models.course import Course
from app.models.student import Student
import datetime

from django.contrib.auth.models import User


class CourseTestClass(TestCase):
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

    def test_course_created(self):
        print("Method: test_course_created.")
        course = Course.objects.get(id=1)
        self.assertEqual('test-code-213', course.code)

    def test_fields_max_length(self):
        print("Method: test_fields_max_length.")
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('code').max_length
        self.assertEquals(max_length, 100)

    def test_only_login_user_can_access_the_endpoint(self):
        print("Method: test_only_login_user_can_access_the_endpoint.")
        c = Client()
        print(User.email)
        logged_in = c.post(
            '/api/login/', {'username': 'test', 'password': 'top_secret'})

        response = c.get('/api/courses/')
        print(response)

        self.assertEqual(response.status_code, 200)


class StudentTestClass(TestCase):
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

    def test_course_created(self):
        print("Method: test_course_created.")
        student = Student.objects.get(id=1)
        self.assertEqual(student.user.username, 'test')

    def test_only_login_user_can_access_the_endpoint(self):
        print("Method: test_only_login_user_can_access_the_endpoint.")
        c = Client()
        logged_in = c.post(
            '/api/login/', {'username': 'test', 'password': 'top_secret'})

        response = c.get('/api/students/')

        self.assertEqual(response.status_code, 200)
