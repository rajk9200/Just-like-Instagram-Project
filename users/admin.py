# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Users,UserProfile,File_upload

# Register your models here.
admin.site.register(Users)
admin.site.register(UserProfile)
admin.site.register(File_upload)
