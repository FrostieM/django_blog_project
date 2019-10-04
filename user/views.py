from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import get_form


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
    username = request.GET.get('username', None)
    form = get_form(page[:-1], None)
    page_type = page[:-1]

    current_blog = Blog.objects.get(user__username=username)
    posts = list(Post.objects.filter(blog=current_blog, type=page_type).order_by('created').all())

    for post in posts:
        post.likes = PostLike.objects.filter(post=post).count()

    html = render_to_string(f"user/{page}.html", {
        'main_post': posts.pop() if posts else None,
        'posts': posts,
        'form': form,
        'type': page_type,
        'creator': request.user.username == username,
    })
    return HttpResponse(html)


@csrf_exempt
def add_post(request, page):
    if request.method == 'POST':
        form = get_form(page, request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse('username', kwargs={
        'username': request.user.username
    }))
