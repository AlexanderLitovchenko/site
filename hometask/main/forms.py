from django import forms
from .models import Campaign, Houses, People
from django.forms import ModelForm



class CampaignForm(ModelForm):
	class Meta:
		model = Campaign
		fields = '__all__'

class HousesForm(ModelForm):
	class Meta:
		model = Houses
		fields = '__all__'

class PeopleForm(ModelForm):
	class Meta:
		model = People 
		fields = '__all__'
