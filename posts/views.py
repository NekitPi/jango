from django.shortcuts import render
from .models import Post, PostTag


def posts(request):
    posts = Post.objects.all()
    tags = PostTag.objects.all()
    return render(request, "index_posts.html", context={"posts": posts,
                                                        "tags": tags})