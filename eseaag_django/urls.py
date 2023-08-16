
from django.contrib import admin
from django.urls import path

from student_manager.views import accommodations
from student_manager.views import home
from student_manager.views import display_teachers
from student_manager.views import delete_all_teachers
from student_manager.views import add_specific_teacher
from student_manager.views import seed_teacher_db
from student_manager.views import teacher_json
from student_manager.views import add_student_accomms
from student_manager.views import add_student
from student_manager.views import delete_all_student_profiles
from student_manager.views import add_student_accomms
from student_manager.views import display_students




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home' ),
    path('seed_teacher_db/', seed_teacher_db, name="seed_teacher_db"),
    path('add_student/', add_student, name="add_student" ),
    path('add_teacher/<str:first_name>_<str:last_name>', add_specific_teacher, name='add_specific_teacher,' ),
    path('display_teachers/', display_teachers, name='display_teachers' ),
    path('display_students/', display_students, name='display_students' ),
    path('accommodations/', accommodations, name="accommodations"),
    path('teacher_json/', teacher_json, name="teacher_json"),
    path('add_student_accomms/', add_student_accomms, name="add_student_accomms" ),
    path('delete_all_teachers/', delete_all_teachers, name='delete_all_teachers' ),
    path('delete_all_student_profiles/', delete_all_student_profiles, name="delete_all_student_profiles" )
    
]
