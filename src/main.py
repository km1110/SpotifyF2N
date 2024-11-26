import spotipy

from oauth import authenticate_spotify
from utils import (
    get_active_device_id,
    display_playlists,
    get_track_in_playlist,
    play_playlist_with_skip,
)


def main():
    access_token = authenticate_spotify()
    sp = spotipy.Spotify(auth=access_token)

    device_id = get_active_device_id(sp)

    playlist_id = display_playlists(sp)

    track_uris, track_titles = get_track_in_playlist(sp, playlist_id)

    wait_seconds = [10 + i * 2 for i in range(len(track_uris))]

    play_playlist_with_skip(sp, device_id, track_uris, track_titles, wait_seconds)


if __name__ == "__main__":
    main()
