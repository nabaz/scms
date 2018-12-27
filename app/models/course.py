from django.db import models
from app.models.base_mixin import BaseMixin

class Course(BaseMixin):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=100)
    starting_date = models.DateField()
    ending_date = models.DateField()

    class Meta:
        verbose_name = 'Course'

