from . import views
from django.urls import path
app_name = 'movieapp'

urlpatterns = [
    path('',views.movies,name= 'movies'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('addmovies',views.add_movies,name='addmovies'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
    

]