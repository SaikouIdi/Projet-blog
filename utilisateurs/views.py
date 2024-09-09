from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import InscriptionForm, ProfileForm
from .models import Profile



class InscriptionView(CreateView):
    form_class = InscriptionForm
    template_name = 'utilisateurs/inscription.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return redirect(self.success_url)
    

@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'utilisateurs/user_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'utilisateurs/user_profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile