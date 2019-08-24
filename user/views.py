from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

from .models import Blog, User


def template_redirect(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return HttpResponseRedirect(reverse('username', kwargs={
        'username': request.user.username
    }))


def blog(request, username):
    user = get_object_or_404(User, username=username)
    get, created = Blog.objects.get_or_create(user=user)

    user_blog = get or created

    return render(request, 'user/blog.html', {
        'username': username,
        'blog': user_blog,
        'creator': request.user.username == username,
    })


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def change_page(request):
    page = request.GET.get('page', None)
    html = render_to_string(f"user/{page}/{page}.html")
    return HttpResponse(html)

