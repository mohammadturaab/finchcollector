from turtle import mode
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import NBA, Player
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class NBAList(TemplateView):
    template_name = 'nbalist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['nbas'] = NBA.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context['nbas'] = NBA.objects.all()
            context['header'] = "NBA Teams"
        return context

class NBA_Create(CreateView):
    model = NBA
    fields = ['name', 'img', 'season_wins', 'season_losses']
    template_name = 'nba_create.html'
    def get_success_url(self):
        return reverse('nba_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect('/teams/')

class NBADetail(DetailView):
    model = NBA
    template_name = "nba_detail.html"

class NBAUpdate(UpdateView):
    model = NBA
    fields = ['name', 'img', 'season_wins', 'season_losses']
    template_name = 'nba_update.html'
    success_url = '/teams/'
    def  get_success_url(self):
        return reverse('nba_detail', kwargs={'pk': self.object.pk})

class NBADelete(DeleteView):
    model = NBA
    template_name = "nba_delete.html"
    success_url = '/teams/'

def profile(request, username):
    user = User.objects.get(username=username)
    nba = NBA.objects.filter(user=user)
    return render (request, 'profile.html',
    {'username': username, 'nbas': nba})

def players_index(request):
    players = Player.objects.all()
    return render (request, 'players_index.html', {'players': players})

def players_show(request, player_id):
    player = Player.objects.get(id=player_id)
    return render (request, 'players_show.html',{'player': player})

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'
    template_name = 'player_form.html'
    success_url = '/player'

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'position']
    template_name = 'player_update.html'
    success_url = '/player'

class PlayerDelete(DeleteView):
    model = Player
    template_name = 'player_confirm_delete.html'
    success_url = '/player'