# from datetime import date
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.urls import reverse
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
    ordering = ["-date"]

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query[:3]
        return data

class PostsListView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

class PostDetailView(DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_post = self.object
        request = self.request
        slugs = request.session.get("stored_posts")
        if slugs and str(loaded_post.slug) in slugs:
            context["is_saved"] = True
        else:
            context["is_saved"] = False
        return context
    

class CommentFormView(View):
    def get(self, request):
        form = CommentForm()
        return render(request, "blog/form.html", {
            "form": form
        })
    
    def post(self, request, slug):
        form = CommentForm(request.POST, request.FILES)
        com_post = Post.objects.get(slug=slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = com_post
            comment.save()
            return redirect(com_post.get_absolute_url())

        return render(request, "blog/form.html", {
            "form": form
        })
    
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
        else:
            context["posts"] = Post.objects.filter(slug__in=stored_posts)

        return render(request, "blog/stored-posts.html", context=context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_slug = str(request.POST["post_slug"])

        if post_slug not in stored_posts:
            stored_posts.append(post_slug)
        else:
            stored_posts.remove(post_slug)

        request.session["stored_posts"] = stored_posts
        
        return redirect(reverse("post", args=[post_slug]))

# def index(request):
#     preview_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {"posts": preview_posts})


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/posts.html", {"posts": all_posts})


# def post(request, slug):
#     sel_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post.html", {"post": sel_post})
