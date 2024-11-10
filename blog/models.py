from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator 

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", default="")
    date = models.DateField()
    slug = models.SlugField(unique=False)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post", args=[self.slug])
    
    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    comment_text = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    profile_pic = models.ImageField(upload_to="profiles", null=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name="comments")