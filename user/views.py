from django.shortcuts import render
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
    user = User.objects.get(username=username)
    blog = Blog.objects.get_or_create(user=user)

    logout(request)
    return render(request, 'user/did_it.html', {
        'username': username,
        'blog': blog,
        'creator': user == request.user,
    })

