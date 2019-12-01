from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.login, name='login'),
    path('profile/',views.profile, name='profile'),
    path('updateprofile/<int:id>/',views.editprofile, name='update_profile'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('mail/',views.mymail, name='mail'),
    path('updateuser/<int:id>/',views.update_user, name='updateuser'),
    path('files/',views.file_show, name='files'),

]