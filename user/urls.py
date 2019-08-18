from django.urls import path
from . import views

urlpatterns = [
    path('', views.template_redirect),
    path('.<str:username>', views.did_it, name='username'),
]
