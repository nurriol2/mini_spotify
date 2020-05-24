#!/usr/bin/env python3

import sys
import spotipy
import spotipy.util as util
from credentials import Credentials
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyAccount:

    def __init__(self):
        self.client_id = Credentials["client_id"]
        self.client_secret = Credentials["client_secret"]
        self.username = Credentials["username"]
        self.token = Credentials["token"]
        self.spotify = spotipy.Spotify(auth=self.token)
        return

    def create_playlist(self, playlistName):
        self.spotify.user_playlist_create(self.username, playlistName)
        return

    def get_track_id(self, q):
        try:
            results = self.spotify.search(q=q, limit = 10, type="track")
            trackid = results["tracks"]["items"][0]["id"]
        except:
            trackid = "7Dju1FHuCiOlOkIXyNYKOU" #calentamiento global
        return [trackid]

    def get_playlist_id(self, playlist):
        playlistid = ''
        playlists = self.spotify.user_playlists(self.username)
        for p in playlists["items"]:
            if p["name"] == playlist:
                playlistid += p["id"]
        return playlistid

    def add_tracks_to(self, p, q):
        trackid = self.get_track_id(q)
        playlistid = self.get_playlist_id(p)
        self.spotify.user_playlist_add_tracks(self.username, playlistid, trackid)
        return
