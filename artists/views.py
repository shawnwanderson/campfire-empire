from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from models import Artist
#  from models import Artist

# Create your views here.

def index(request):
    return render(request, "artists/index.html")

def artist(request, username):
    artist = get_object_or_404(User, username=username)
    artist_name = artist.first_name + " " + artist.last_name
    user = request.user
    context = {'artist':artist, 'artist_is_user':False, 'artist_name':artist_name}
    if(artist == user):
        context['artist_is_user'] = True
    artist = Artist.objects.get(user=artist)
    return render(request, "artists/artist.html", context)
    #  artist = get_object_or_404(User, user.id=user_id)
    #  return render(request, "artists/artist.html", {"artist":artist})
