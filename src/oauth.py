import os
from dotenv import load_dotenv

from spotipy.oauth2 import SpotifyOAuth


def authenticate_spotify():
    load_dotenv()

    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    REDIRECT_URI = os.environ["REDIRECT_URI"]

    # スコープ設定
    SCOPE = os.environ["SCOPE"]

    print("Spotifyにログインしています...")
    print("crient_id: ", CLIENT_ID)

    # Spotify認証設定
    sp_oauth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_path=".cache",
    )

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        # 認証URLを生成
        auth_url = sp_oauth.get_authorize_url()
        print("認証URLにアクセスして認証してください:\n", auth_url)

        # 認証後のリダイレクト先URLを入力
        redirect_response = input("\nリダイレクト後のURLを貼り付けてください: ")
        code = sp_oauth.parse_response_code(redirect_response)

        # アクセストークンを取得
        token_info = sp_oauth.get_access_token(code)

    access_token = token_info["access_token"]

    return access_token
