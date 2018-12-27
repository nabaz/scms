from rest_framework import viewsets
from app.models.student import Student
from app.serializers.student_serializer import StudentSerializer
from rest_framework import generics, filters


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (filters.SearchFilter,)
    # Search by Name (Title) I usually would love to use this extension just give me more control https://github.com/philipn/django-rest-framework-filters
    search_fields = ('=name',)

