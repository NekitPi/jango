from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, PostTag


def posts(request):
    posts = Post.objects.all()
    tags = PostTag.objects.all()
    return render(request, "index_posts.html", context={"posts": posts,
                                                        "tags": tags})


def get_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponse(f"<h1>Пост с  id {id} не существует</h1>")
    return render(request, "post_detail.html", context={"post": post})


def get_tag_post(request, title):
    try:
        tag = PostTag.objects.get(title=title)
    except PostTag.DoesNotExist:
        return HttpResponse(f"<h1>Тэг с таким названием {title} не найден! </h1>")

    return render(request, "tag_info.html", context={"tag": tag,
                                                     "title": title})