from django.shortcuts import render
from app.controllers import getTrackInfo, getToken
from app.models import Track, TRACKS

# Create your views here.
def roomView(request):
  token = 'Bearer ' + getToken()
  # FIXME must build list from tracklist
  t1 = getTrackInfo('28kOGtTZzbfQ8fMmTwjRFq', token)
  t2 = getTrackInfo('3vv9phIu6Y1vX3jcqaGz5Z', token)
  TRACKS.append(Track(t1['name'], t1['artists'], t1['img_url']))
  TRACKS.append(Track(t2['name'], t2['artists'], t2['img_url']))
  tracks = {
    'tracks' : TRACKS
  }
  return render(request, 'app.html', tracks)