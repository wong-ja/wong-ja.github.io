import streamlit.components.v1 as components

def show_spotify_playlist(playlist_id: str):
    playlist_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"
    components.iframe(playlist_url, width=700, height=380)
