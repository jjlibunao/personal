import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import streamlit as st

# Initialize the Spotipy client with API credentials on local machine
client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Starting the Streamlit app
st.title('Spotify Song Recommender')

# Get user input for a song title
song_name = st.text_input('Enter a song title (song name only, no artist):', 'OMG')

# Search for the track ID of the input song
results = sp.search(q='track:' + song_name, type='track')
if len(results['tracks']['items']) == 0:
    st.warning('No tracks found.')
    st.stop()
track_id = results['tracks']['items'][0]['id']

# Use the audio features to find similar tracks
related_tracks = sp.recommendations(seed_tracks=[track_id], limit=10)

# Display the recommended tracks
st.write(f'Recommended tracks based on "{song_name}":')
for i, track in enumerate(related_tracks['tracks']):
    album = track['album']['name']
    st.write(f"{i+1}. {track['name']} by {track['artists'][0]['name']} ({album})")

    seconds, milliseconds = divmod(track['duration_ms'], 1000)
    minutes, seconds = divmod(seconds, 60)
    url = track["external_urls"]
    indent = "&nbsp;" * 10
    st.markdown(f'<p style="font-size:15px; margin: 0px; margin-top: -18px;">{indent}{minutes}:{seconds:02d} min, <a href="{url}" style="text-decoration:none;color:blue;">Listen</a></p>', unsafe_allow_html=True)