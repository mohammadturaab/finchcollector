from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('teams/', views.NBAList.as_view(), name='nbalist'),
    path('teams/new/', views.NBA_Create.as_view(), name="nba_create"),
    path('teams/<int:pk>/', views.NBADetail.as_view(), name="nba_detail"),
    path('teams/<int:pk>/update', views.NBAUpdate.as_view(), name='nba_update'),
    path('teams/<int:pk>/delete', views.NBADelete.as_view(), name='nba_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('players/', views.players_index, name='players_index'),
    path('players/<int:player_id>/', views.players_show, name='players_show'),
    path('player/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
]