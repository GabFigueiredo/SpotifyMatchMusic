import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from google import genai

# --- SPOTIFY ---
client_id = '3e38317449e84311ba371c37c41feaaa'
client_secret = '40e286bc493c4978864a525c900ae87e'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
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

GEMINI_API_KEY = 'AIzaSyC3r45qQIaYc3t0Wbw0rBJEm2pHHfE-a58' 

client = genai.Client(api_key=GEMINI_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents= prompt
)

print("Resposta do Gemini:")
print(response.text)
