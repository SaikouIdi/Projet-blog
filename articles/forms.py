from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tags', 'image']

       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nom")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")