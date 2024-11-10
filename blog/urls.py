from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("posts/<slug:slug>/add-comment", views.CommentFormView.as_view(), name="comment"),
    path("posts/", views.PostsListView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post")
]
