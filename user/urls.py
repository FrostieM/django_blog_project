from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.template_redirect),
    path('.<str:username>', views.blog, name='username'),
    path('logout', views.user_logout, name='user_logout'),
    path('change_page', views.change_page, name='change_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
