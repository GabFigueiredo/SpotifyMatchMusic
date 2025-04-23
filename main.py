import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from google import genai

from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_link = 'https://open.spotify.com/playlist/6DpZmGIT3RniGZjIPZmZlv?si=vGgfxGHbQK-Xq-iJ3W9LKw&pi=7e6oNPc7Sa2Nf'
playlist_uri = playlist_link.split("/")[-1].split("?")[0]  # Corrigido

# --- PEGAR MÚSICAS ---
results = sp.playlist_tracks(playlist_uri)

ListaDeMusicas = []
for item in results['items']:
    track = item['track']
    name = track['name']
    artist = track['artists'][0]['name']
    ListaDeMusicas.append(f"{name} - {artist}")  # Corrigido: removido `track` do print

# --- GEMINI ---
TemaDoDia = "Chamados a frutificar em Cristo"

prompt = f"""
Considere a seguinte lista de músicas:

{chr(10).join(ListaDeMusicas)}

O tema do dia é: "{TemaDoDia}"

Tópicos relacionados a esse tema:

1. Permanência real, não aparência religiosa  
2. Libertação da autossuficiência  
3. Frutos visíveis, duradouros e espirituais  
4. Quebrar ciclos de religiosidade estéril  
5. Que o processo leve à semelhança com Cristo

Para cada um dos tópicos acima, liste apenas os nomes das músicas da lista que se relacionam com ele.  
Não explique, apenas liste.
"""

client = genai.Client(api_key=GEMINI_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents= prompt
)

print("Resposta do Gemini:")
print(response.text)
