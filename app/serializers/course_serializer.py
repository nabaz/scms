from app.models.course import Course
from app.serializers.student_serializer import StudentSerializer
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'code', 'name', 'students', 'starting_date', 'ending_date','created_at', 'updated_at')
        depth=1

