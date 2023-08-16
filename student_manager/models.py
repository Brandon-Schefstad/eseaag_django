from django.db import models

# Create your models here.
class Student(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=12)
    id = models.CharField(max_length = 12, primary_key=True)
    grade = models.ForeignKey('Grade', on_delete=models.DO_NOTHING)
    primary_exceptionality = models.CharField(max_length=20)
    secondary_exceptionality = models.CharField(max_length=20, blank=True)
    case_manager = models.ForeignKey('Teacher', on_delete=models.CASCADE, blank=True)

    iep_due_date = models.DateField()

    def __str__(self):
      return self.first_name + ' ' +  self.last_name

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=31)
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    def __str__(self):
      return self.first_name + ' ' +  self.last_name

class Accommodation(models.Model):
    DOMAIN_CHOICES = [('DOMAIN_PRESENTATION','Presentation'),('DOMAIN_RESPONSE','Response'),('DOMAIN_SETTING','Setting'),('DOMAIN_SCHEDULING','Scheduling'),]
    name = models.CharField(max_length=30)
    domain = models.CharField(max_length=20, choices=DOMAIN_CHOICES)
    subdomain = models.CharField(max_length=40)
    students = models.ManyToManyField('Student', through="Accommodation_List")
    def __str__(self):
        return self.name
    
class Accommodation_List(models.Model):
   student = models.ForeignKey("Student", on_delete=models.CASCADE)
   accommodation = models.ForeignKey("Accommodation", on_delete=models.CASCADE)
   date_added = models.DateField()

class Grade(models.Model):
   name = models.CharField(max_length=8)
   def __str__(self):
    return self.name

