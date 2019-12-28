from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MyProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField()
    birthday = forms.DateField()
    city = forms.CharField()
    country = forms.CharField()
    club = forms.CharField()
    status = forms.CharField()
    gender = forms.CharField()
    phone_no = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'birthday', 'city',
                  'country', 'club', 'status', 'gender', 'phone_no']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = ['image']
