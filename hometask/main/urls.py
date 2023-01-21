from django.urls import path
from .views import *

urlpatterns = [
	path('home/', home, name = 'home'),
	path('profile/<int:current_user>', profile, name = 'profile'),
	path('campaigns/', campaigns, name= 'campaigns'),
	path('campaigns/<int:current_camp>', camp_profile, name = 'camp_profile'),
	path('create_camp/', create_camp, name = 'create_campaign'),
	path('addperson/', add_person, name = 'add_person'),
	path('editcamp/<int:pk>', edit_camp, name = 'edit_camp'),
	path('addadress', add_adress, name = 'add_adress'),
	path('delete_campaign/<int:pk>/', delete_camp, name = 'delete_camp'),
	path('delete_person/<int:pk>/', delete_people_from_camp, name = 'delete_person'),
	path('delete_adress/<int:pk>/', delete_adress_from_camp, name = 'delete_adress'),
	path('editperson/<int:pk>', edit_person, name = 'edit_person'),
	path('editadress/<int:pk>', edit_adress, name = 'edit_adress'),
]