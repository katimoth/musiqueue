import requests
import json
import base64
from app.admin import client_id, client_secret

def get_track(trackid, token):
  headers = {
    'Authorization': token
  }
  response = requests.get(f'https://api.spotify.com/v1/tracks/{trackid}', headers=headers)
  return response.json()

def get_token():
  credentials = f'{client_id}:{client_secret}'
  cred_bytes = credentials.encode('ascii')
  base64_bytes = base64.b64encode(cred_bytes)
  base64_string = base64_bytes.decode('ascii')
  headers = {
    'Authorization': 'Basic ' + base64_string
  }
  data = {
    'grant_type': 'client_credentials'
  }
  response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data).json()
  return response['access_token']