from django.urls import path
from . import views

urlpatterns = [
    path('', views.template_redirect),
    path('.<str:username>', views.blog, name='username'),
    path('logout', views.user_logout, name='user_logout'),
    path('change_page', views.change_page, name='change_page')
]
