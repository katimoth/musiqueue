from django.db import models

# Create your models here.
class Track:
  def __init__(self, name, artists, img_url):
    self.name = name
    self.artists = artists
    self.img_url = img_url
    self.votes = 0
  
  def inc_votes(self):
    self.votes += 1

  def dec_votes(self):
    self.votes -= 1

TRACKS = []