from flask import Flask, request
from waitress import serve
import uuid

import ytdlp_service
from cache import Cache
import config

app = Flask(__name__)

ytdlp = ytdlp_service.YtdlpService()
cache = Cache('appserver:')

@app.route('/health')
def index():
    return {
        'status': 'ok'
    }

@app.route('/api/v1/youtube/info')
def get_youtube_info():
    url = request.args.get('url')

    log_base = {
        'request_id': request.headers.get('X-Request-ID') or str(uuid.uuid4()),
        'source_ip': request.remote_addr or 'unknown',
        'path': request.path,
        'method': request.method,
        'headers': dict(request.headers),
        'args': dict(request.args),
    }

    # Log
    log_base['message'] = '= = = Request start = = ='
    print(log_base)

    # MEMO: キャッシュを使う
    info = cache.get(url)
    if info is not None:
        log_base['message'] = 'Cache hit'
        print(log_base)

        return info

    if url is None:
        return {
            'error': 'URL is required'
        }, 400

    info = ytdlp.get_info(url)

    # MEMO: キャッシュを使う
    cache.set(url, info)

    log_base['message'] = 'Request end'
    print(log_base)

    return info

@app.route('/api/v1/cache/all')
def get_cache_all():
    return cache.all()

if __name__ == '__main__':
    serve(app, host=config.APP_HOST, port=config.APP_PORT)
