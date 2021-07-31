from django.shortcuts import render
from app.controllers import get_track_info, get_token

# Create your views here.
def app(request):
  token = 'Bearer ' + get_token()
  # FIXME must build list from tracklist
  tracks = {
    'tracks' : [get_track_info('28kOGtTZzbfQ8fMmTwjRFq', token), get_track_info('3vv9phIu6Y1vX3jcqaGz5Z', token),]
  }
  return render(request, 'app.html', tracks)