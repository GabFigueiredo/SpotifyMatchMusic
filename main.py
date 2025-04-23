import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import google.generativeai as genai

client_id = '3e38317449e84311ba371c37c41feaaa'
client_secret = '40e286bc493c4978864a525c900ae87e'

auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)

sp = spotipy.Spotify(auth_manager = auth_manager)

playlist_link = 'https://open.spotify.com/playlist/6DpZmGIT3RniGZjIPZmZlv?si=vGgfxGHbQK-Xq-iJ3W9LKw&pi=7e6oNPc7Sa2Nf'

playlist_uri = playlist_link.split("/")
[-1].split("?")[0]

results = sp.playlist_tracks(playlist_uri)

ListaDeMusicas = []
for item in results['items']:
    track = item['track']
    name = track['name']
    artist = track['artists'][0]['name']
    ListaDeMusicas.append(f"{track}, {name} - {artist}")

results = sp.playlist_tracks(playlist_uri)

TemaDoDia = "Chamados a frutificar em Cristo"

GEMINI_API_KEY = ''

genai.configure(api_key = GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

prompt = f"""
Considere esta lista de músicas:

{chr(10).join(ListaDeMusicas)}


"""

response = model.generate_content(prompt)

print("Resposta do Gemini:")
print(response.text)