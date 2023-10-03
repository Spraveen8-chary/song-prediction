'''
devotional : https://open.spotify.com/playlist/79csyq71DCxtgizRQhcuPQ?si=ea8babdf87174901
love : https://open.spotify.com/playlist/37i9dQZF1DWTGda3Eyqjzr?si=99896ebee7134d09
happy : https://open.spotify.com/playlist/37i9dQZF1DX2UT3NuRgcHd?si=36f817671350464b
party : https://open.spotify.com/playlist/37i9dQZF1DWZdcdjsv83gQ?si=4dad03a398284a0f
breakup : https://open.spotify.com/playlist/2YLo1pyOZK0WZtCpMC4mIW?si=e45345f9f7d24da3
romantic : https://open.spotify.com/playlist/5mE2sNh330ItJh3MsUshOW?si=2b72faf8fa6a46a8
'''


import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your Spotify API credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET_ID'
REDIRECT_URI = 'http://localhost:8080'
# Set up authentication# This should match the redirect URI in your Spotify App settings

# Authenticate and create a Spotify API object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='playlist-read-private'))  # Add necessary scopes

playlist_data = {
    '2YLo1pyOZK0WZtCpMC4mIW': 'breakup',
    '37i9dQZF1DWTGda3Eyqjzr': 'love',
    '37i9dQZF1DX2UT3NuRgcHd': 'happy',
    '37i9dQZF1DWZdcdjsv83gQ': 'party',
    '5mE2sNh330ItJh3MsUshOW': 'romantic',
    '79csyq71DCxtgizRQhcuPQ': 'devotional'
}
songs = []

for playlist_id, theme in playlist_data.items():
    results = sp.playlist_tracks(playlist_id)
    
    # print(f"\n******************Songs from the '{theme}' playlist:*******************\n")
    
    for item in results['items']:
        track = item['track']
        # print(track['name'])
        songs.append({'Theme' : theme , 'Song Name' : track['name']})

# Close the authentication session
sp.auth_manager.get_access_token()

import pandas as pd 

data = pd.DataFrame(songs)
print(data)
data.to_csv('playlist_data.csv', index=False)
