from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Users
from .models import Campaign, Houses, People
from django.http import HttpResponse

from .forms import CampaignForm, HousesForm, PeopleForm
from django.contrib import messages

from django.contrib.auth.models import User



@login_required(login_url = 'login')
def home(request):
	title = 'Домашняя страница'
	return render(request, 'main/home.html', {'title':title})


def profile(request, current_user):
	title = 'Мой профиль'	
	current_user_id = Users.objects.get(pk = current_user)
	context = {'current_user_id' : current_user_id, 'title':title}
	return render(request, 'main/profile.html', context)


def campaigns(request):
	title = 'Все кампании'
	camps = Campaign.objects.all()
	context = {'camps' : camps, 'title':title}
	return render(request, 'main/campaigns.html', context)

def camp_profile(request, current_camp):
	title = 'Профиль кампании'
	current_camp = Campaign.objects.get(pk = current_camp)

	people = People.objects.filter(to_camp = current_camp)
	houses = Houses.objects.filter(to_camp = current_camp)
	context = {'current_camp' : current_camp, 'people':people, 'houses':houses, 'title':title}
	return render(request, 'main/camp_profile.html', context)

def create_camp(request):
	title = 'Создать кампанию'
	camp_all = Campaign.objects.all()
	form = CampaignForm()
	if request.method == 'POST':
		form = CampaignForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('camp_name')
			messages.success(request, f'Кампания {name} успешно создана')
			return redirect('campaigns')
	context = {'form' : form, 'camp_all':camp_all, 'title':title}
	return render(request, 'main/createcamp.html', context)


def edit_camp(request, pk):
	title = 'Изменить'
	camp = Campaign.objects.get(id = pk)
	form = CampaignForm(instance = camp)
	if request.method == 'POST':
		form = CampaignForm(request.POST, instance = camp)
		if form.is_valid():
			form.save()
			return redirect('campaigns')
	context = {'form':form, 'camp': camp, 'title':title}
	return render(request, 'main/edit_campaign.html', context)

def edit_person(request, pk):
	title = 'Изменить'
	person = People.objects.get(id = pk)
	form = PeopleForm(instance = person)
	if request.method == 'POST':
		form = PeopleForm(request.POST, instance = person)
		if form.is_valid():
			form.save()
			return redirect('campaigns')
	context = {'form':form, 'person': person, 'title':title}
	return render(request, 'main/edit_person.html', context)

def edit_adress(request, pk):
	title = 'Изменить'
	adress = Houses.objects.get(id = pk)
	form = HousesForm(instance = adress)
	if request.method == 'POST':
		form = HousesForm(request.POST, instance = adress)
		if form.is_valid():
			form.save()
			return redirect('campaigns')
	context = {'form':form, 'adress': adress, 'title':title}
	return render(request, 'main/edit_adress.html', context)


def add_person(request):
	title = 'Добавить человека'
	form = PeopleForm()
	if request.method == 'POST':
		form = PeopleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('campaigns')
	context = {'form' : form,'title':title }
	return render(request, 'main/addperson.html', context)

def add_adress(request):
	title = 'Добавить адрес'
	form = HousesForm()
	if request.method == 'POST':
		form = HousesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('campaigns')
	context = {'form' : form, 'title':title}
	return render(request, 'main/addadress.html', context)

def delete_camp(request, pk):
	title = 'Удалить кампанию'
	camp = Campaign.objects.get(id = pk)
	if request.method == "POST":
		camp.delete()
		return redirect('campaigns')
	context = {'camp':camp, 'title':title}
	return render(request, 'main/delete_campaign.html', context)



def delete_people_from_camp(request, pk):
	title = 'Удалить человека'
	person = People.objects.get(id = pk)
	if request.method == 'POST':
		person.delete()
		return redirect('campaigns')
	context = {'person' : person, 'title':title}
	return render(request, 'main/delete_person.html', context)

def delete_adress_from_camp(request, pk):
	title = 'Удалить адресс'
	adress = Houses.objects.get(id = pk)
	if request.method == 'POST':
		adress.delete()
		return redirect('campaigns')
	context = {'adress' : adress, 'title':title}
	return render(request, 'main/delete_adress.html', context)