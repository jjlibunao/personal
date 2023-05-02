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

# Generates a playlist based on the recommended songs
# redirect_uri = 'http://localhost:8501/callback'
# scope = 'user-library-modify'
# sp_oauth = SpotifyOAuth(client_id=client_id,
#                         client_secret=client_secret,
#                         redirect_uri=redirect_uri,
#                         scope=['playlist-modify-private'])
# auth_manager = None
# user_name = None
# st.write('If you would like to save this playlist, please log in.')
# if st.button('Log in with Spotify'):
#     auth_manager = spotipy.oauth2.SpotifyOAuth.get_auth_manager(sp_oauth)
#     user_name = sp.current_user()['id']
# if user_name:

#     playlist_name = f'Recommended tracks based on "{song_name}"'
#     playlist_description = f'Automatically generated playlist based on "{song_name}".'
#     playlist = sp.user_playlist_create(user=user_name, 
#                                     name=playlist_name, 
#                                     public=False, 
#                                     description=playlist_description)
#     track_uris = [track['uri'] for track in related_tracks['tracks']]
#     sp.user_playlist_add_tracks(user=user_name, playlist_id=playlist['id'], tracks=track_uris)
#     st.write(f'The playlist "{playlist_name}" has been created for {user_name} with {len(related_tracks["tracks"])} tracks.')
# elif auth_manager:
#     st.warning('Invalid credentials, please try again.')