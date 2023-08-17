from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register, name='register'), #perfiles
	path('profile/<str:username>/', views.profile, name='profile'), #perfiles
	path('editar/', views.editar, name='editar'), #perfiles

    #seccion aun no testeada
    
	path('follow/<str:username>/', views.follow, name='follow'),
	path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
]