from django import forms
from .models import Users,UserProfile
class SignupForm(forms.ModelForm):
    class Meta:
        model = Users
        fields ='__all__'

    email = forms.EmailField(
        label='Your Email :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email',
            }
        )
    )
    mobile = forms.CharField(
        label='Your Mobile :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email',
            }
        )
    )
    password = forms.CharField(max_length=100,
                               label='Your Password :',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Enter Your Password',
                                   }
                               )
                               )

    name = forms.CharField(
        label='username :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email',
            }
        )
    )


        # fields =('name')


class LoginForm(forms.Form):
    email =forms.EmailField(
        label='Your Email :',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Email',
            }
        )
    )
    password =forms.CharField(max_length=100,
                              label='Your Password :',
                              widget=forms.PasswordInput(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Enter Your Password',
                                  }
                              )
                              )



class ProfleForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_image','fname')
