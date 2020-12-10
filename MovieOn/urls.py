from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('movies/', views.list_movies, name='movies'),
    path('directors/', views.list_directors, name='directors'),
    path('genre/', views.list_genres, name='genres'),
    path('movies/add', views.add_movie, name='add_movie'),
    path('movies/edit/<int:movie_id>', views.edit_movie, name='edit_movie'),
    path('director/add', views.add_director, name='add_director'),
    path('director/edit/<int:director_id>', views.edit_director, name='edit_director'),
    path('director/delete/<int:director_id>', views.delete_director, name='delete_director'),
    path('genres/add', views.add_genre, name='add_genre'),
    path('genres/edit/<int:genre_id>', views.edit_genre, name='edit_genre'),
    path('genres/delete/<int:genre_id>', views.delete_genre, name='delete_genre'),
]
