from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def bloglist(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'bloglist.html', {'posts': posts})


def posts(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, 'posts.html', {'post': post})