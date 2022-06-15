from youtube_client import YouTubeClient

def run():
#1. Get a list of our pplaylists from YouTube
youtube_client = YouTubeClient('./creds/client_secret.json')
#2. Ask which playlist we want to get the music videos from

#3. For each video in the playsli, get the song information from YouTube

#4. Search forthe song on Spotify

#5. If we found the song, add it to our Spotify liked songs

if __name__ == '__main__':
    run()