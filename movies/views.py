from django.shortcuts import render, redirect
from .models import Movie, Score, Genre
from django.db.models import Avg

# Create your views here.
def index(request):
    # a = Movie.objects.filter(title='title')
    # movies = Movie.objects.all()
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    # print(movies_genre)
    return render(request, 'index.html',{'movies': movies})

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    scores = movie.score_set.all
    context = {
        'movie':movie,
        'scores':scores
    }
    return render(request, 'detail.html', context)
    
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')

def scnew(request, movie_pk):
    if request.method == "POST":
        movie = Movie.objects.get(pk=movie_pk)
        score = Score()
        score.content = request.POST.get('content')
        score.score =  request.POST.get('score')
        score.movie = movie
        # score = Score(content=content, score=score)
        score.save()
    return redirect('movies:detail', movie_pk)
    
def scdel(request, movie_pk, score_pk):
    if request.method == "POST":
        score = Score.objects.get(pk=score_pk)
        score.delete()
    return redirect('movies:detail', movie_pk)
    # movie.pk 가 아닌 movie_pk 를 넘겨줘야함.
    
    
    
def edit(request, movie_pk):
    if request.method == 'POST':
        genre_id = request.POST.get('genre')
        genre = Genre.objects.get(pk = genre_id)
        movie = Movie.objects.get(pk=movie_pk)
        movie.genre = genre
        movie.title = request.POST.get('title')
        movie.description = request.POST.get('description')
        movie.audience = request.POST.get('audience')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        movie = Movie.objects.get(pk=movie_pk)
        genres = Genre.objects.all()
        context = {
            'movie':movie,
            'genres':genres
            }
        return render(request, 'edit.html', context)
    
def update(request, pk):
    u_movie = Movie.objects.get(pk=pk)
    u_movie.title = request.POST.get('title')
    u_movie.audience = request.POST.get('audience')
    u_movie.genre = request.POST.get('genre')
    u_movie.score = request.POST.get('score')
    u_movie.poster_url = request.POST.get('poster_url')
    u_movie.description = request.POST.get('description')
    # u_movie = Movie(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url, description=description)
    u_movie.save()
    return redirect('/movies/')