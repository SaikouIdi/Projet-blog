from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return(self.name)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        tags_list = ", ".join([tag.name for tag in self.tags.all()])
        return f'{self.title} - {self.category.name} - {tags_list}'


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Commentaire de {self.user.username} sur {self.article}"
