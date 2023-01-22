from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Users


def index(request):
	return HttpResponse('index')


def register_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
	
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				userfn = form.cleaned_data.get('first_name')
				userln = form.cleaned_data.get('last_name')
				messages.success(request, 'Учетная запись была создана для ' + userfn, userln)
				return redirect('login')
		context = {'form' : form}
	return render(request, 'users/register_page.html', context)

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
	
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				userfn = form.cleaned_data.get('first_name')
				userln = form.cleaned_data.get('last_name')
				messages.success(request, 'Учетная запись была создана для ' + userfn, userln)
				return redirect('login')
			else:
				messages.error(request, 'Что-то пошло не так')
		context = {'form' : form}
	return render(request, 'users/register.html', context)

def login_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Неверное "имя пользователя" и/или пароль')

	return render(request, 'users/login.html')

def logout_user(request):
	logout(request)
	return redirect('login')

def update_profile(request, pk):
	user = Users.objects.get(id = pk)
	form = CreateUserForm(instance = user)
	if request.method == 'POST':
		form = CreateUserForm(request.POST, instance = user)
		if form.is_valid():
			form.save()
			return redirect('home')
			#message
	context = {'form' : form, 'user' : user}
	return render(request, 'users/update_profile.html', context)

def delete_user(request, pk):
	title = 'Удалить профиль'
	user = Users.objects.get(id = pk)
	if request.method == "POST":
		logout(request)
		user.delete()
		return redirect('login')
	context = {'user':user, 'title':title}
	return render(request, 'users/delete_user.html', context)
