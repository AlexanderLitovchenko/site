from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Users

class CreateUserForm(UserCreationForm):
	class Meta:
		model = Users
		fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 
				'phone', 'password1', 'password2']
		date_of_birth = forms.DateField()
		phone = forms.IntegerField()


