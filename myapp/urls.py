from django.contrib import admin
from django.urls import path, include 
from . views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", some, name="some"),
    path('signin/', signin, name='signin'),

#Hod views
    path('add_course',add_course,name='addcourse'),
    path('add_course_save',add_course_save,name='addcoursesave'),
    path('add_staff',add_staff,name='addstaff'),
    path('add_staff_save',add_staff_save,name='addstaffsave'),
    path('add_class',add_class,name='addclasse'),
    path('add_class_save',add_class_save,name='addclassesave'),
    path('add/',add, name='add'),
    path('add/addrecord/', addrecord, name='addrecord'),
#     path('add_subject',add_subject,name="addsubject"),
#     path('add_subject_save',add_subject_save,name='addacademicadvisor'),
#     path('add_aadvisor',add_aadvisor,name="addsubject"),
#     path('add_aadvisor_save',add_aadvisor_save,name='addacademicadvisorsave'),
#     path('advisor_save',advisor_save,name='advisor_save'),

#     path('time_table',time_table,name='addcourse'),
# # personalinfo page

#     path('per_info/', per_info, name='per_info'),
#     path('per_info/pinfo/', pinfo, name='pinfo'),

# # staff
# #staff_leave
#     path('staff_leave_view/',staff_leave_view,name='staff_leave_view'),
#     path('staff_leave_view/staff_leave_approve/<int:leave_id>',staff_leave_approve,name='staff_leave_approve'),
#     path('staff_leave_view/staff_leave_reject/<int:leave_id>',staff_leave_reject,name='staff_leave_reject'),
#     path('take_attendance',take_attendance,name="take_attendance"),
#     path('attendance_save',attendance_save,name="attendance_save"),
#     path('sachiev/', sachiev, name='sachiev'),
#     path('sachiev/sachievment/', sachievment, name='sachievment'),
#     path('student_mark/',student_mark,name="student_mark"),
#     path('student_mark_save',student_mark_save,name="student_mark_save"),
#     path('scholarship', scholarship, name='scholarship'),
#     path('scholarship_save', scholarship_save, name='scholarship'),
#     path('attend',attend,name="attend"),
    
# # Registerpage
#     path('rg/', rgstr, name='ref'), 

# # signin

#     path('signin/', signin, name='signin'),
# #student
#     path('student_apply_leave/',student_apply_leave,name='student_apply_leave'),
#     path('student_apply_leave/student_apply_leave_save/',student_apply_leave_save,name='student_apply_leave_save'),
#     path('student_apply_leave/student_view_leave/',student_view_leave,name='student_view_leave'),
#     path('student_apply_leave/student_view_leave/student_view_leave_show',student_view_leave_show,name='student_view_leave_show'),
#     path('student_view/',student_view,name="student_view"),
#     path('student_view_save/',student_view_save,name="student_view_save"),
#     path('select_eccc/',select_eccc,name="select_eccc")

]