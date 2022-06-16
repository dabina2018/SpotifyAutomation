import os

from GitRepos.SpotifyAutomation.spotify_client import SpotifyClient
from youtube_client import Playlist, YouTubeClient

def run():
#1. Get a list of our playlists from YouTube
youtube_client = YouTubeClient('./creds/client_secret.json')
spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTHTOKEN'))
playlists = youtube_client.get_playlists()

#2. Ask which playlist we want to get the music videos from
for index, playlist in enumerate(playlists):
    print(f"{index}: {playlist.title}")
choice = int(input("Enter your choice"))
chosen_plalist = playlists[choice]
print(f"You selected: {chosen_playlist.title}")

#3. For each video in the playlist, get the song information from YouTube
songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
print(f"Attempting to add {len(songs)}")

#4. Search forthe song on Spotify
for song in songs:
    spotify_song_id = spotify_client.search_song(song.artists, song.track)
    if spotify_song_id:
        added_song = spotify_client.add_song_to_spotify()
        if added_song: 
            print(f"Added{song.artist}")


#5. If we found the song, add it to our Spotify liked songs

if __name__ == '__main__':
    run()