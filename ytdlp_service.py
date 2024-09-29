import yt_dlp

import cache

class YtdlpService:
    def __init__(self):
        self.ydl = yt_dlp.YoutubeDL()
        self.cache = cache.Cache('ytdlp:')

    # 入力されたURLの動画タイトルを取得する
    def get_info(self, url):
        info = self.cache.get(url)
        if info is None:
            info = self.ydl.extract_info(url, download=False)
            self.cache.set(url, info)

        return {
            'id': info.get('id', None),
            'title': info.get('title', None),
            'description': info.get('description', None),
            'original_url': info.get('original_url', None),
            'channel': info.get('channel', None),
            'channel_url': info.get('channel_url', None),
            'duration': info.get('duration', None),
            'thumbnail': info.get('thumbnail', None),
        }


# テスト
if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=ELFFjFVLjGo'
    ytdlp = YtdlpService()
    title = ytdlp.get_info(url)
