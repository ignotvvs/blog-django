# from datetime import date
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
#from django.views.generic.edit import CreateView
# from lorem_text import lorem
from .models import Post
from .forms import CommentForm

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

class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("-date")[:3]
        return data

class PostsListView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

class PostDetailView(DetailView):
    template_name = "blog/post.html"
    model = Post

class CommentFormView(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, "blog/form.html", {
            "form": form
        })
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)
        post_slug = self.kwargs.get("slug")
        com_post = Post.objects.get(slug=post_slug)

        if form.is_valid():
            form.instance = form.save(commit=False)
            form.instance.post = com_post
            form.instance.save()
            return redirect(com_post.get_absolute_url())

        return render(request, "blog/form.html", {
            "form": form
        })

# def index(request):
#     preview_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {"posts": preview_posts})


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/posts.html", {"posts": all_posts})


# def post(request, slug):
#     sel_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post.html", {"post": sel_post})
