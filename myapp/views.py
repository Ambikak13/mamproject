import re
from django.shortcuts import render
from email import message
import email
from multiprocessing import context
from tokenize import Name
from unicodedata import category
from urllib import request
from venv import create
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from myapp.EmailBackEnd import EmailBackEnd

# Create your views here.
def some(request):
    return render(request,"s1/login.html")

def signin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return render(request,"s1/admin.html")
                
            elif user_type == '2':
                return render(request,"s1/staff.html")
                
            # elif user_type == '3':
            #     # return HttpResponse("Student Login")
            #     return redirect('student_home')
            # else:
            #     messages.error(request, "Invalid Login!")
            #     return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return HttpResponseRedirect("/some/")
            # return redirect('login')

def add_course(request):
  return render(request,"s1/addcourse.html")

def add_course_save(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
   
  else:
    course=request.POST.get("Name")
    cid=request.POST.get("course_id")
    dept=request.POST.get("dept")
    try:
      course_model=courses(course_id=cid,Name=course,dept=dept)
      course_model.save()
      print("Successfuly added course")
      return HttpResponse(request,"Successfuly added course")
      return HttpResponseRedirect("s1/add_course")
    except:
      print("faild to added course")
      return HttpResponse(request,"Failed to add course")
      return HttpResponseRedirect("s1/add_course")

def add_class(request):
  course=courses.objects.all()
  return render(request,"s1/addclass.html",{"course":course})

def add_class_save(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
   
  else:
    cls=request.POST.get("name")
    cid=request.POST.get("class_id")
    cs=request.POST.get("course")
    course=courses.objects.get(course_id=cs)
    try:
      classs_model=classes(class_id=cid,name=cls,course_id=course)
      classs_model.save()
      print("Successfuly added class")
      return HttpResponse(request,"Successfuly added course")
      return HttpResponseRedirect("s1/add_course")
    except:
      print("faild to added course")
      return HttpResponse(request,"Failed to add course")
      return HttpResponseRedirect("s1/add_course")

def add_staff(request):
  course=courses.objects.all()
  #stf=staff.objects.all()
  context={
    "course":course,
#"stf":stf
  }
  return render(request,"s1/addstaff.html",context)

def add_staff_save(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
   
  else:
    first_name = request.POST.get('staff_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    sid=request.POST.get("staff_id")
    id=request.POST.get("course")
    course=courses.objects.get(course_id=id)
    print(id)
    try:
      print("loop")
      user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
      print(user)
      user.staffs.staff_id=sid
      user.staffs.staff_name=first_name
      user.staffs.course_id=course
      user.save()
      print("Successfuly added class")
      return HttpResponse(request,"Successfuly added staff")
      return HttpResponseRedirect("s1/add_course")
    except:
      print("faild to added staff")
      return HttpResponse(request,"Failed to add staff")
      return HttpResponseRedirect("s1/add_course")

def add(request):
  course=courses.objects.all()
  cls=classes.objects.all()
  context={
    'course':course,
    'cls':cls
  }
  return render(request,'s1/addstudent.html',context)


def addrecord(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
  else:
    fn = request.POST.get('first_name')
    ln = request.POST.get('last_name')
    em=request.POST.get('email')
    un=request.POST.get('username')
    pwd=request.POST.get('password')
    rn = request.POST.get('rno') 
    gn=request.POST.get('gender')
    cl=request.POST.get('cls')
    sc=request.POST.get('sec')
    cs=request.POST.get('course')
    try:
      user = CustomUser.objects.create_user(username=un, password=pwd, email=em, first_name=fn, last_name=ln, user_type=3)
      studs=stud.objects.all()
      user.studs.rno=rn
      user.studs.first_name=fn
      user.studs.last_name=ln
      user.studs.sclass=cl
      user.studs.gender=gn
      user.studs.email=em
      user.studs.section=sc
      user.studs.course=cs
      user.save()
      print("added")
      return HttpResponseRedirect(request,"s1/addstudent.html")
      messages.success(request,"succesffuly added")
    except:
      print("does not added")
      return HttpResponseRedirect(request,"s1/addstudent.html")