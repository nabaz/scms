from app.models.base_mixin import BaseMixin
from django.db import models
from django.contrib.auth.models import User


class Student(BaseMixin):
    gender_choices = [('M', 'Male'), ('F', 'Female')]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField('Course', related_name='students')
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
