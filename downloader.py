from pathlib import Path

import yt_dlp

class YoutubeManager:
    def __init__(self):
        self.ydl_opts = {
            'quiet': False,
            'remote_components': 'ejs:github'
            }
        self.videos = []
        self.query = ""

    def getvids(self, query):
        self.query = query
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            list_vid = ydl.extract_info(f"ytsearch5:{query}", download=False)
            self.videos = list_vid.get('entries', [])
            return [self._extract_info(video) for video in self.videos]

    def _extract_info(self, video):
        title = video.get('title', 'unknown')
        publisher = video.get('uploader', 'unknown')
        duration_secs = video.get('duration', 0)
        url = video.get('webpage_url', 'unknown')

        if duration_secs:
            mins = duration_secs // 60
            secs = duration_secs % 60
            duration = f'{mins}:{secs:02d}'
        else:
            duration = 'unknown'

        return {
            'title': title,
            'uploader': publisher,
            'duration': duration,
            'url': url
        }
    
    def download_video(self, url):
        download_dir = Path.home() / 'Downloads'
        if not download_dir.is_dir():
            download_dir = Path.home()

        download_opts = {
            'quiet': False,
            'outtmpl': str(download_dir / '%(title)s.%(ext)s'),
        }
        
        with yt_dlp.YoutubeDL(download_opts) as ydl:
            ydl.download([url])