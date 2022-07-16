from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class courses(models.Model):
    course_id=models.AutoField(primary_key=True,max_length=20)
    Name=models.CharField(max_length=25)
    dept=models.CharField(max_length=30)
    objects = models.Manager()

class staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    staff_name=models.CharField(max_length=25)
    course_id=models.ForeignKey(courses,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class stud(models.Model):
    rno = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sclass = models.CharField(max_length=25)
    section  = models.CharField(max_length=10)
    gender = models.CharField(max_length=50)
    DOB = models.DateField(default='1998-01-01')
    profile_pic=models.ImageField()
    academic_advisor=models.CharField(max_length=25)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    address= models.CharField(max_length=50)
    achievements=models.CharField(max_length=100)
    scholarship=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    midday_meal=models.CharField(max_length=20)
    course=models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class parent(models.Model):
    parent_id=models.AutoField(primary_key=True)
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    contact=models.IntegerField()
    email=models.CharField(max_length=30)
    objects = models.Manager()

class classes(models.Model):
    class_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=15)
    course_id=models.ForeignKey(courses,on_delete=models.CASCADE)
    objects = models.Manager()

class subjects(models.Model):
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    subject_id=models.CharField(primary_key=True,max_length=20)
    subject=models.CharField(max_length=50)
    class_id=models.ForeignKey(classes,on_delete=models.CASCADE)
    objects = models.Manager()

class mark(models.Model):
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subjects,on_delete=models.CASCADE)
    marks=models.CharField(max_length=3)
    category=models.CharField(max_length=20)
    objects = models.Manager()

class attendance(models.Model):
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subjects,on_delete=models.CASCADE)
    attendance_date=models.DateField()
    status=models.IntegerField(default=0)
    objects = models.Manager()

class application(models.Model):
    appn_status=models.IntegerField(default=0)
    appn_id=models.AutoField(primary_key=True)
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    distance=models.CharField(max_length=3)
    income_status=models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class eccc(models.Model):
    eccc_id=models.AutoField(primary_key=True)
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    eccc_course=models.CharField(max_length=25)
    choice1=models.CharField(max_length=25)
    choice2=models.CharField(max_length=25)
    choice3=models.CharField(max_length=25)
    no_of_seats=models.IntegerField()
    objects = models.Manager()

class notification(models.Model):
    n_id=models.AutoField(primary_key=True,max_length=20)
    message=models.CharField(max_length=50)
    notification_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class leave(models.Model):
    leave_id=models.AutoField(primary_key=True)
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    leave_reason=models.CharField(max_length=100)
    leave_date=models.DateField()
    leave_status=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            staff.objects.create(admin=instance,course_id=courses.objects.get(id=1),staff_id="",staff_name="")
            
        if instance.user_type == 3:
            stud.objects.create(admin=instance)
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.studs.save()