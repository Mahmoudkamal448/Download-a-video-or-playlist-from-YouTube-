from pytube import YouTube, Playlist

# Set the URL of the video or playlist
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object for the video or playlist
if "playlist" in url:
    yt = Playlist(url)
else:
    yt = YouTube(url)

# Download the video or playlist
if "playlist" in url:
    for video in yt.videos:
        video.streams.get_highest_resolution().download()
else:
    yt.streams.get_highest_resolution().download()
