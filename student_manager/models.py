from django.db import models

# Create your models here.
class Student(models.Model):
    GRADE_CHOICES = [('GRADE_K','Kindergarten'),
                     ('GRADE_1','First'),
                     ('GRADE_2','Second'),
                     ('GRADE_3','Third'),
                     ('GRADE_4','Fourth'),
                     ('GRADE_5','Fifth'),
                     ('GRADE_6','Sixth'),
                     ('GRADE_7','Seventh'),
                     ('GRADE_8','Eighth'),
                     ('GRADE_9','Ninth'),
                     ('GRADE_10','Tenth'),
                     ('GRADE_11','Eleventh'),
                     ('GRADE_12','Twelfth ')]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length = 12)
    grade = models.CharField(max_length=8, choices=GRADE_CHOICES)
    primary_exceptionality = models.CharField(max_length=20)
    secondary_exceptionality = models.CharField(max_length=20, blank=True)
    caseManager = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING)
    iep_due_date = models.DateField()
    #TODO Accommodations table
    accommodations = models.ManyToManyField('Accommodation')
    def __str__(self):
      return self.first_name + ' ' +  self.last_name

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
      return self.first_name + ' ' +  self.last_name

class Accommodation(models.Model):
    DOMAIN_CHOICES = [('DOMAIN_PRESENTATION','Presentation'),('DOMAIN_RESPONSE','Response'),('DOMAIN_SETTING','Setting'),('DOMAIN_SCHEDULING','Scheduling'),]
    domain = models.CharField(max_length=20, choices=DOMAIN_CHOICES)
    subdomain = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
