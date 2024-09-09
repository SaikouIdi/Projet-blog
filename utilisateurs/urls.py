from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.InscriptionView.as_view(), name='sinscrire'),
    path('connexion/', auth_views.LoginView.as_view(template_name='utilisateurs/connexion.html', next_page='article_list'), name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='article_list'), name='deconnexion'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
]
