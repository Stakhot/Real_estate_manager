from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.property_list, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name=''), name='logout'),
    path('add/', views.add_property, name='add_property')
]

