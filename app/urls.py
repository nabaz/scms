import rest_framework
from django.contrib.auth.models import User
from app.serializers.course_serializer import CourseSerializer
from rest_framework.routers import DefaultRouter
from app.viewsets.course_viewset import CourseViewSet
from app.viewsets.student_viewset import StudentViewSet
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register('api/courses', CourseViewSet)
router.register('api/students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]
