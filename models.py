# IMPORT DJANGO MODELS
from django.db import models

# Create your models here.
class DjangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    CourseNumber = models.IntegerField()
    InstructorName = models.CharField(max_length=60)
    Duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    # object manager
    objects = models.Manager()

