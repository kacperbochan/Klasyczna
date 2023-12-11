from pytube import Playlist, YouTube
from moviepy.editor import *

id = 0

def download_and_convert_audio(url, path):
    global id
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    mp4_file = audio.download(output_path=path, filename=f"{id}.mp4")
    mp3_file = mp4_file.replace('.mp4', '.mp3')
    audio_clip = AudioFileClip(mp4_file)
    audio_clip.write_audiofile(mp3_file)
    audio_clip.close()
    os.remove(mp4_file)  # Remove the original MP4 file
    id += 1
    return mp3_file

def download_playlist(playlist_url, path):
    pl = Playlist(playlist_url)
    for video_url in pl.video_urls:
        print(f"Downloading and converting {video_url}")
        download_and_convert_audio(video_url, path)

# Example usage
playlist_url = 'https://www.youtube.com/playlist?list=PLcBHyPoMP6eXyfPnM-og4wgQsT_RWjIIw'  # Replace with your YouTube playlist URL
path = './music'  # Replace with the path where you want to download the videos
download_playlist(playlist_url, path)
