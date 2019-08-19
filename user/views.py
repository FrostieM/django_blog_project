from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Blog, User


def template_redirect(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return HttpResponseRedirect(reverse('username', kwargs={
        'username': request.user.username
    }))


def did_it(request, username):
    # TODO get_or_404page do next time
    user = get_object_or_404(User, username=username)
    get, created = Blog.objects.get_or_create(user=user)

    blog = get or created

    return render(request, 'user/blog.html', {
        'username': username,
        'blog': blog,
        'creator': request.user.username == username,
    })


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

