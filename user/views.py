from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import HttpResponseNotFound

from .models import *
from .forms import get_form


def template_redirect(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return HttpResponseRedirect(reverse('username', kwargs={
        'username': request.user.username,
    }))


def blog(request, username, page='videos'):
    user = get_object_or_404(User, username=username)
    get, created = Blog.objects.get_or_create(user=user)
    user_blog = get or created

    return render(request, 'user/blog.html', {
        'username': username,
        'blog': user_blog,
        'creator': request.user.username == username,
        'page': page,
    })


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def change_page(request):
    if request.is_ajax() and request.method == 'GET':
        page = request.GET.get('page', None)
        username = request.GET.get('username', None)
        form = get_form(page[:-1], None)
        page_type = page[:-1]

        current_blog = Blog.objects.get(user__username=username)
        posts = list(Post.objects.filter(blog=current_blog, type=page_type).order_by('-created').all())

        for post in posts:
            post.likes = PostLike.objects.filter(post=post).count()

        html = render(request, f"user/{page}.html", {
            'main_post': posts.pop(0) if posts else None,
            'posts': posts,
            'form': form,
            'type': page_type,
            'creator': request.user.username == username,
        })
        return HttpResponse(html)
    return HttpResponseNotFound('Not found')


def add_post(request, page):
    if request.is_ajax() and request.method == 'POST':
        form = get_form(page, request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('upload')
        return HttpResponse("Unsupported file type", status=500)
    return HttpResponseNotFound('Not found')


def delete_post(request):
    if request.is_ajax() and request.method == 'GET':
        post_id = request.GET['postId']
        post = Post.objects.get(id=post_id, blog__user__username=request.user)
        post.delete()
        return HttpResponse('deleted')
    return HttpResponseNotFound('Not found')
