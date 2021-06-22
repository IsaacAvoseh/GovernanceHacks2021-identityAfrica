from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class Register(UserCreationForm):
    first_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields= ('username', 'first_name', 'email','password1', 'password2')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('last_name','img','phone', 'country', 'state', 'id_card', 'bvn', )