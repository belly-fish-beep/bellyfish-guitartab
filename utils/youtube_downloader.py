import yt_dlp
import os

def download_youtube_audio(link, output_path="audio/yt_audio.wav"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    
    return output_path
