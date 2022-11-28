from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *



class MembersForm(ModelForm):
	class Meta:
		model = Members
		fields = '__all__'
		exclude = ['user']


class BookingsForm(ModelForm):
    class Meta: 
        model = Bookings
        fields = '__all__'
        exclude =['user']

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username','email','password1','password2']

class ArtsForm(ModelForm):
    class Meta:
        model = Arts
        fields = '__all__'

class ExhibitionsForm(ModelForm):
    class Meta:
        model = Exhibitions
        fields = '__all__'
       
