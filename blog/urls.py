from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
#from django.conf import settings #para imagenes
# from django.conf.urls.static import static #para imagenes


urlpatterns = [
	path('', views.home, name='home'), #blog
	path('delete/<int:post_id>/', views.delete, name='delete'), #blog
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	

]