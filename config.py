import os

def get_env(key, default):
    value = os.environ.get(key)
    if value is None:
        return default
    return value

APP_HOST = get_env('APP_HOST', '0.0.0.0')
APP_PORT = int(get_env('APP_PORT', '8080'))

