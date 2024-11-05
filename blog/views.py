# from datetime import date
from django.shortcuts import get_object_or_404, render

# from django.http import HttpResponseNotFound
# from lorem_text import lorem
from .models import Post

# posts_list = [
#     {
#         "id": "misty-esoterica",
#         "title": "Misty's Esoterica",
#         "content": lorem.paragraphs(5),
#         "date_update": date(2077, 4, 10),
#         "description": lorem.words(20),
#         "photo": "misty.jpg"
#     },{
#         "id": "dogtown",
#         "title": "Dogtown District",
#         "content": lorem.paragraphs(5),
#         "date_update": date(2077, 9, 20),
#         "description": lorem.words(20),
#         "photo": "dogtown.png"
#     }
# ]

# Create your views here.


def index(request):
    preview_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": preview_posts})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/posts.html", {"posts": all_posts})


def post(request, slug):
    sel_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post.html", {"post": sel_post})
