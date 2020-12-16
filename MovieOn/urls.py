from django.urls import path
from MovieOn.controllers import homepage_controller, director_controller, genre_controller, movie_controller, registration_controller


urlpatterns = [
    path('', homepage_controller.index, name='index'),
    path('register', registration_controller.index, name='register'),
    path('movies/', movie_controller.index, name='movies'),
    path('movies/<query>/page/<page_number>', movie_controller.pagination, name='pagination'),
    path('directors/', director_controller.index, name='directors'),
    path('genre/', genre_controller.index, name='genres'),
    path('movies/add', movie_controller.add_movie, name='add_movie'),
    path('movies/edit/<int:movie_id>', movie_controller.edit_movie, name='edit_movie'),
    path('director/add', director_controller.add_director, name='add_director'),
    path('director/edit/<int:director_id>', director_controller.edit_director, name='edit_director'),
    path('director/delete/<int:director_id>', director_controller.delete_director, name='delete_director'),
    path('genres/add', genre_controller.add_genre, name='add_genre'),
    path('genres/edit/<int:genre_id>', genre_controller.edit_genre, name='edit_genre'),
    path('genres/delete/<int:genre_id>', genre_controller.delete_genre, name='delete_genre'),
]
