from django.shortcuts import render
from django.http import HttpResponseNotFound
from lorem_text import lorem

posts_list = [
    {
        "id": "misty-esoterica",
        "title": "Misty's Esoterica",
        "content": lorem.paragraphs(4),
        "date_update": "10 Apr 2077",
        "description": lorem.words(50),
        "photo": "blog/images/misty.jpg"
    },{
        "id": "dogtown",
        "title": "Dogtown District",
        "content": lorem.paragraphs(4),
        "date_update": "20 Sep 2077",
        "description": lorem.words(20),
        "photo": "blog/images/dogtown.png"
    }
]

# Create your views here.

def index(request):
    preview_posts = None
    if len(posts_list):
        preview_posts = posts_list[0:3]
    return render(request, "blog/index.html", {"posts": preview_posts})

def posts(request):
    return render(request, "blog/posts.html", {
        "posts": posts_list
    })

def post(request, slug):
    try:
        sel_post =next(item for item in posts_list if item["id"] == slug)
        return render(request, "blog/post.html", {
            "post_title": sel_post["title"],
            "post_content": sel_post["content"],
            "post_date": sel_post["date_update"],
            "post_pic" : sel_post["photo"]

        })
    except KeyError:
        return HttpResponseNotFound("Wrong name")