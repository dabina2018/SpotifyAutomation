import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import youtube_dl

class Playlist(object):
    def __init__(self,id,title):
        self.id = id
        self.title = title

class Song(object):
    def __init__(self, artist, track):
        self.artist = artist
        self.track = track

class Playlist(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title

class YoutubeClient(object):
    def __init__(self, credentials_location):
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        ## Disable OAuthlib's HTTPS verificaiton when running locally.
        ## *DO NOT* leave this otion enabled in production
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        ## client_secrets_file = client_secret_79755140115-qutu1i5rvebf85e33ar0ll8mnnjarka9.apps.googleusercontent.com.json

        #Get credentials and crea an API  client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            credentials_location, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        self.youtube_client = youtube_client

        ##request = youtube.channels().list(    )
        ##response = request.execute()



    def get_playlists(self):
        request = self.youtube_client.playlists()list(
            part="id, snippet",
            maxResults=50,
            mine=True
        )
        response = request.execute()
        playlists = [Playlist(item['id'], item['snippet']['title']) for item in response ['items']]

        return playlists


    def get_videos_from_playlist(self, playlist_id):
        songs = []

        request = self.youtube_client.playlistItems().list(
            playlistId=playlist_id,
            part="id, snippet"
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            artist, track = self.get_artist_and_track_from_video(video_id)
            if artist and track:
                songs.append(Song(artist, track))

        return artist, track


    def get_artist_and_track_from_video(self, video_id):

        youtube_url = f"https://www.youtube.com/watch?v={video_id}"

        video = youtube_dl.YoutubeDL({'quiet': True}).extract_info(
            youtube_url, download=False
        )

        artist = video['artist]']
        track = video["track"]

        return artist, track
