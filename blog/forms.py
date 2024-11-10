from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        #fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "comment_text": "Your Comment",
            "rating": "Your Rating",
            "profile_pic": "Your Picture"
        }