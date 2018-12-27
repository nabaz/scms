from rest_framework import viewsets
from app.models.course import Course
from app.models.student import Student
from app.serializers.course_serializer import CourseSerializer
from app.serializers.student_serializer import StudentSerializer
from rest_framework import serializers, filters

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.SearchFilter,)
    # Search by Name (Title) I usually would love to use this extension just give me more control https://github.com/philipn/django-rest-framework-filters
    search_fields = ('=name', '=starting_date')
