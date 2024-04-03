from django.shortcuts import redirect, render
from .models import Movies
from .forms import MovieForm

# Create your views here.

def movies(request):
    movie = Movies.objects.all()
    return render(request,'index.html',{'movies' : movie})
def details(request,movie_id):
    movies = Movies.objects.get(id=movie_id)
    return render(request,'details.html',{'movies': movies})
def add_movies(request):
    if request.method == 'POST':
        movie = request.POST['moviename']
        year = request.POST['year']
        des = request.POST['des']
        image = request.FILES['image']
        movies = Movies(movie= movie,year=year,des=des,image=image)
        movies.save()

    return render(request,'addmovies.html')
def update(request,id):
    movies = Movies.objects.get(id=id)
    form =MovieForm(request.POST or None,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movies':movies})


def delete(request,id):
    if request.method == 'POST':
        movies=Movies.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')