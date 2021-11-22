from django.shortcuts import render

# Create your views here.
from blog.models import Post


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})