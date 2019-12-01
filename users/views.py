from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm,ProfleForm
from django.contrib import messages
from .models import Users,UserProfile,File_upload

from django.core.mail import send_mail


# Create your views here.
def profile(request):
    login_user='not Login'
    if not request.session.get('myemail',None):
         return redirect('login')
    else:
        login_user = request.session.get('myemail')

    signup_obj =Users.objects.get(email=login_user)



    profile=UserProfile.objects.filter(user=signup_obj)

    context ={
        'login_user':login_user,
        'profile':profile,
    }
    return render(request,'users/profile.html',context)

def login(request):
    email=None
    login_form =LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')

        signup =Users.objects.filter(email=email,password=password)
        if signup.exists():
            request.session['myemail']=email
            return redirect('profile')

            print('match')
        else:
            messages.success(request,'email or password Not match')
            print('not match')

    context ={
        'login_form':login_form,

    }

    res = render(request,'users/login.html',context)
    res.set_cookie('email',email)
    return res

def signup(request):
    s =Users.objects.all()

    signup_form =SignupForm(request.POST or None)
    if signup_form.is_valid():
        signup_form.save()

        return redirect('signup')

        print('data stored')
    context ={
        'signup_form':signup_form,
        's':s,
    }


    return render(request,'users/signup.html',context)

def logout(request):
    del request.session['myemail']
    return redirect('login')



def mymail(request):

    send_mail("Hello Biplab", "How are You?", "biplabdebnathindian@gmail.com", ['biplabdebnathindian@gamil.com'])
    mail_send="Your mail send successfuly"

    return render(request,'users/mail.html',{'mail_send':mail_send})


def editprofile(request,id):
    signup_id = Users.objects.get(id=id)
    form =ProfleForm(request.POST or None ,instance=signup_id )
    if form.is_valid():
        form.save()

        return redirect('profile')
    context ={
        'form':form,
    }
    return render(request,'users/edit_profile.html',context)


def update_user(request,id=None):
    singup_id =Users.objects.get(id=id)

    signup_form = SignupForm(request.POST or None, instance=singup_id)
    if signup_form.is_valid():
        signup_form.save()
        return redirect('signup')
    context ={
        'signup_form':signup_form,
    }
    return render(request,'users/signup.html',context)



def file_show(request):
    file = File_upload.objects.all()

    context = {

        'file': file,
    }
    return render(request, 'users/file.html', context)