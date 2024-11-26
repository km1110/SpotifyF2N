import time


def get_active_device_id(sp):
    devices = sp.devices()
    if not devices["devices"]:
        print(
            "アクティブなデバイスが見つかりません。Spotifyアプリを開いて再生可能なデバイスをアクティブにしてください。"
        )
        exit()

    device_id = devices["devices"][0]["id"]

    return device_id


def display_playlists(sp):
    print("\n保存済みプレイリスト:")
    playlists = sp.current_user_playlists(limit=50)
    for idx, item in enumerate(playlists["items"]):
        print(f"{idx + 1}: {item['name']} (ID: {item['id']})")

    # 再生したいプレイリストを選択
    playlist_id = input("\n再生したいプレイリストのIDを入力してください: ")

    return playlist_id


def get_track_in_playlist(sp, playlist_id):
    # プレイリスト内の楽曲を取得して再生
    tracks = sp.playlist_tracks(playlist_id)
    track_uris = [track["track"]["uri"] for track in tracks["items"]]
    track_titles = [track["track"]["name"] for track in tracks["items"]]

    # 楽曲名とユニークなIDを表示
    print("\nプレイリスト内の楽曲:")
    for idx, track in enumerate(tracks["items"]):
        track_info = track["track"]
        print(f"{idx + 1}: {track_info['name']} (ID: {track_info['id']})")

    return track_uris, track_titles


def play_playlist_with_skip(sp, device_id, track_uris, track_titles, wait_seconds):
    if track_uris:
        for i in range(len(track_uris)):
            # 現在のトラックを再生
            sp.start_playback(device_id=device_id, uris=[track_uris[i]])
            print(f"トラック「{track_titles[i]}」を再生中...")

            # 指定した時間待機
            wait_second = wait_seconds[i]
            time.sleep(wait_second)

            # 最後のトラックでない場合は次のトラックにスキップ
            if i < len(track_uris) - 1:
                sp.next_track(device_id=device_id)
                print(f"{wait_second}秒経過。次のトラックにスキップしました。")
            sp.next_track(device_id=device_id)
    else:
        print("このプレイリストには再生可能なトラックがありません。")
