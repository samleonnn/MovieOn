from django.urls import path
from MovieOn.controllers import homepage_controller, director_controller, genre_controller, movie_controller, registration_controller, comment_controller


urlpatterns = [
    path('', homepage_controller.index, name='index'),
    path('register/', registration_controller.index, name='register'),
    path('movie/', movie_controller.index, name='movies'),
    path('movie/<query>/page/<page_number>', movie_controller.pagination, name='pagination'),
    path('movie/<imdb_id>', movie_controller.movie_details, name='details_movie'),
    path('director/', director_controller.index, name='directors'),
    path('genre/<slug:genre_slug>', genre_controller.index, name='genres'),
    path('movie/<imdb_id>/comment/edit/<comment_id>', comment_controller.edit_comment, name='edit_comment'),
    path('movie/<imdb_id>/comment/delete/<comment_id>', comment_controller.delete_comment, name='delete_comment'),
]
