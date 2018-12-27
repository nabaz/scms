from app.models.student import Student
from app.models.course import Course
from rest_framework import serializers
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'gender', 'dob', 'courses')
