from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100, unique=True)
    password =models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    mobile = models.CharField(max_length=15)
    verify = models.BooleanField(default=False)
    otp = models.CharField(max_length=20)


    def __str__(self):
        return self.email



class UserProfile(models.Model):

    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    fname = models.CharField(max_length=12, default='First Name')
    lname = models.CharField(max_length=12, default='Last Name')
    profile_image = models.ImageField(default='avatar.png', upload_to='profile')
    cover = models.ImageField(default='cover.png', upload_to='cover')
    status = models.TextField(default='Your Bio')
    profile_status = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    dob = models.CharField(max_length=12,default='DD-MM-YYYY')
    about_me=models.CharField(max_length=100)




    def __str__(self):
        return self.user.name + " - " + self.created.strftime('%d-%m-%y')

#
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=Users)


class SignupMailConfirm(models.Model):
    user =models.ForeignKey(Users,on_delete=models.CASCADE)
    verify_code =models.CharField(max_length=120)


class File_upload(models.Model):
    file_name = models.CharField(max_length=100)
    file =models.FileField(upload_to='upload', default='file')