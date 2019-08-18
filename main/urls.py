from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('sign_in', views.sign_in_page, name='sign_in'),
    path('', include('user.urls')),
]
