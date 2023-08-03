from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
GENDER = (
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("cant't mention", "CAN'T MENTION")
)
from django.db import models

# Create your models here.

GENDER =(
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("don't mention", "DON'T MENTION")
)
class StaffMember(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250, choices=GENDER)
    age = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    department = models.CharField(max_length=250)



class Student(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250, choices=GENDER)



class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    staff = models.CharField(max_length=250)
    head_of_department = models.CharField(max_length=250)
    courses_in_department = models.CharField(max_length=250)


class Club(models.Model):
    club_name = models.CharField(max_length=50)
    head_of_club = models.CharField(max_length=250)
