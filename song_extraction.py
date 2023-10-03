import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import time
import pyautogui

def play_song(selected_theme , selected_songs):
    # Replace these with your Spotify app credentials
   
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_SECRET_ID'
    redirect_uri = 'http://localhost:8080'
        
    playlist_data = {
        '2YLo1pyOZK0WZtCpMC4mIW': 'breakup',
        '37i9dQZF1DWTGda3Eyqjzr': 'love',
        '37i9dQZF1DX2UT3NuRgcHd': 'happy',
        '37i9dQZF1DWZdcdjsv83gQ': 'party',
        '5mE2sNh330ItJh3MsUshOW': 'romantic',
        '79csyq71DCxtgizRQhcuPQ': 'devotional'
    }
    
    playlist_id = None
    for ids, playlist_theme in playlist_data.items():
        if playlist_theme.lower() == selected_theme[0].lower():  
            playlist_id = ids
            break
    
    if playlist_id:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                       client_secret=client_secret,
                                                       redirect_uri=redirect_uri,
                                                       scope='user-modify-playback-state'))
        
        playlist_tracks = sp.playlist_tracks(playlist_id)
        
        predicted_song_uris = []
        for track in playlist_tracks['items']:
            track_name = track['track']['name']
            if any(song.lower() in track_name.lower() for song in selected_songs):
                predicted_song_uris.append(track['track']['uri'])
        print(predicted_song_uris)
        
        if predicted_song_uris:
            random_song_uri = random.choice(predicted_song_uris)
            print("random : ",random_song_uri)
            
            track_uri = random_song_uri.split(":")[2]
            deep_link = f'spotify:track:{track_uri}'
            
            webbrowser.open(deep_link)
            time.sleep(15)
            pyautogui.hotkey('alt', 'tab')
        else:
            print("No matching songs found in the playlist.")
    else:
        print("Selected theme not found in playlist data.")