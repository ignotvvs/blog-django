from datetime import date
from django.shortcuts import render
from django.http import HttpResponseNotFound
from lorem_text import lorem

posts_list = [
    {
        "id": "misty-esoterica",
        "title": "Misty's Esoterica",
        "content": lorem.paragraphs(5),
        "date_update": date(2077, 4, 10),
        "description": lorem.words(20),
        "photo": "misty.jpg"
    },{
        "id": "dogtown",
        "title": "Dogtown District",
        "content": lorem.paragraphs(5),
        "date_update": date(2077, 9, 20),
        "description": lorem.words(20),
        "photo": "dogtown.png"
    }
]

# Create your views here.

def get_date(post_n):
    return post_n['date_update']

def index(request):
    sorted_posts = sorted(posts_list,key=get_date)
    preview_posts = None
    if len(posts_list):
        preview_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": preview_posts})

def posts(request):
    return render(request, "blog/posts.html", {
        "posts": posts_list
    })

def post(request, slug):
    try:
        sel_post = next(item for item in posts_list if item["id"] == slug)
        return render(request, "blog/post.html", {
            "post": sel_post
        })
    except (KeyError, StopIteration):
        return HttpResponseNotFound("wrong")