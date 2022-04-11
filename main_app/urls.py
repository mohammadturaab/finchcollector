from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('teams/', views.NBAList.as_view(), name='nbalist'),
    path('teams/new/', views.NBA_Create.as_view(), name="nba_create"),
    path('teams/<int:pk>/', views.NBADetail.as_view(), name="nba_detail"),
    path('teams/<int:pk>/update/', views.NBAUpdate.as_view(), name="nba_update"),
    path('teams/<int:pk>/delete/', views.NBADelete.as_view(), name="nba_delete"),
    path('user/<username>/', views.profile, name='profile'),

]