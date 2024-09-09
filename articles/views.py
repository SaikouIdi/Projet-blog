from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article, Comment, Category
from .forms import ArticleForm, CommentForm, ContactForm

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = '/'  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html' 
    context_object_name = 'articles'  
    paginate_by = 5


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = '/'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.user = self.request.user
            comment.save()
            return redirect('article_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)
    

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"Message de {name} via le formulaire de contact"
            message_body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL], 
            )
            messages.success(request, "Votre message a été envoyé avec succès.")
            form = ContactForm() 
    else:
        form = ContactForm()

    return render(request, 'articles/contact.html', {'form': form})


def navbar_view(request):
    categories = Category.objects.all()
    return render(request, 'articles/navbar.html', {'categories': categories})


def articles_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    return render(request, 'articles/articles_by_category.html', {
        'category': category,
        'articles': articles
    })