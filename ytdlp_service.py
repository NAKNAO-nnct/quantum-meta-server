import yt_dlp

class YtdlpService:
    def __init__(self):
        self.ydl = yt_dlp.YoutubeDL()

    # 入力されたURLの動画タイトルを取得する
    def get_info(self, url):
        info = self.ydl.extract_info(url, download=False)
        return {
            'title': info.get('title', None),
            'description': info.get('description', None),
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
