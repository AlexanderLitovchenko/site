from django.urls import path
from .views import *

urlpatterns = [
	path('', register_page, name = 'register'),
	path('login/', login_page, name = 'login'),
	path('logout/', logout_user, name = 'logout'),
	path('index/', index, name = 'index'), 
	path('update/<int:pk>/', update_profile, name = 'update'),
	path('delete_user/<int:pk>', delete_user, name = 'delete_user'),
	path('register', register, name = 'register_page')

]
