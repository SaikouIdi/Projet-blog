from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    contact_view,
    articles_by_category,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'), 
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/new/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('contact/', contact_view, name='contact'),
    path('category/<int:category_id>/', articles_by_category, name='articles_by_category'),
]

