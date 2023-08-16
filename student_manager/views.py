from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .models import Teacher, Student, Accommodation_List, Grade, Accommodation
from rest_framework.renderers import JSONRenderer, serializers
import datetime


#! Returns a dictionary of accommodations sorted by their domain. 
# !NOTE Django templates do not allow for dynamic key lookup like React
def accommodations(request):
    domain_list = ['DOMAIN_PRESENTATION', 'DOMAIN_RESPONSE','DOMAIN_SCHEDULING','DOMAIN_SETTING']
    accommodations_dict = {}
    for domain in domain_list:
        accommodations_dict[domain] = Accommodation.objects.filter(domain=domain)
    return render(request, 'accommodations.html', {"accommodations":accommodations_dict})

def display_teachers(request):
    all_teachers = Teacher.objects.all()
    if all_teachers:
        return render(request,"teacher_detail.html", {'teachers':all_teachers})
    else:
        return render(request,"teacher_detail.html", {'message':'No Teachers :('})

def display_students(request):
    all_students = Student.objects.all()
    if len(all_students) > 0:
        return render(request,"student_detail.html", {"students":all_students})
    else:
        return render(request,"student_detail.html", {"message":"No Students"})

def add_specific_teacher(request, first_name, last_name):
    teacher = Teacher(first_name=first_name, last_name=last_name)
    teacher.save()
    all_teachers = Teacher.objects.all()
    return render(request, 'teacher_detail.html', {'teachers':all_teachers})

#! Helper function to seed database without needing to load in a CSV. 
def seed_teacher_db(request):
    if len(Teacher.objects.all())==0:
        a = Teacher.objects.create(first_name="Brandon", last_name="Schefstad")
        b = Teacher.objects.create(first_name="Cheyenne", last_name="Atkinson")
        c = Teacher.objects.create(first_name="Johnny", last_name="FakeTeacher")
        print(a,b,c)    
    if len(Grade.objects.all()) == 0:
        seed_grade_db(request)
    if len(Student.objects.all()) == 0:
        add_student(request)
  
    return HttpResponse(200)

def seed_grade_db(request):
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
    for grade in GRADE_CHOICES:
        grade_to_add = Grade.objects.create(name=grade[0])

#! Hard-coded student
def add_student(request):
    # Better to declare gets outside of construction?
    new_student_grade = Grade.objects.get(name="GRADE_2")
    new_student = Student.objects.create(id="537648", first_name="Johnny", last_name="FakeStudent", 
                            grade=new_student_grade, student_id="537648", primary_exceptionality='DHH', 
                            case_manager=Teacher.objects.get(first_name="Cheyenne"), iep_due_date=str(datetime.date.today()))
    new_student2 = Student.objects.create(id="5376482", first_name="Jerry", last_name="FakeStudentt", 
                            grade=Grade.objects.get(name="GRADE_4"), student_id="5376481", primary_exceptionality='DHH', 
                            case_manager=Teacher.objects.get(first_name="Brandon"), iep_due_date=str(datetime.date.today()))
    
    # When to use () + Save vs .create()
    accomm_list = Accommodation_List(student=new_student2, accommodation=Accommodation.objects.get(id=8), date_added=datetime.date.today())
    accomm_list.save()


def add_student_accomms(request):
    student = Student.objects.get(first_name="Johnny")
    accommodation = Accommodation.objects.get(id=2)
    student.accommodations.add(accommodation)
    student.save()
    return HttpResponse(student.accommodations.all())


def home(request):
    return render(request,"teacher_detail.html", {})

#! Utility class to serialize information. Keys must match the model
class TeacherSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name= serializers.CharField(max_length=200)
    full_name= serializers.CharField(max_length=200)
#! Practice using serializers to return JSON data 
def teacher_json(request):
    teachers =Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    json={}
    if serializer.data:
        json = JSONRenderer().render(serializer.data)
    else:
        json = JSONRenderer().render({"message":"No Teachers For That Search"})
    return HttpResponse(json)


def delete_all_student_profiles(request):
    Student.objects.all().delete()
    print('Deleting All Students')
    return HttpResponse(200)

def delete_all_teachers(request):
    Teacher.objects.all().delete()
    t = len(Teacher.objects.all())
    return HttpResponse(t)