from django.shortcuts import render
from app.controllers import get_track, get_token

# Create your views here.
def app(request):
  token = 'Bearer ' + get_token()
  tracks = {
    'tracks' : [get_track('28kOGtTZzbfQ8fMmTwjRFq', token), get_track('3vv9phIu6Y1vX3jcqaGz5Z', token),]
  }
  return render(request, 'app.html', tracks)