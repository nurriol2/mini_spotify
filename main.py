#!/usr/bin/env python3

from account import SpotifyAccount
from parse_songlist import Songlist

#spotipy.exceptions.SpotifyException

def main():

    #song = "one in a million dance gavin dance"
    #song = "88834738951135633371"
    myAcc = SpotifyAccount()
    #r = myAcc.get_track_id(song)
    #print(r)
    myAcc.create_playlist("test1")

    mySonglist = Songlist("/Users/nikourriola/Desktop/projects/mini_spotify/smallsonglist.txt").get_querylist()

    for song in mySonglist:
        myAcc.add_tracks_to("test1", song)

    #myAcc.create_playlist("test0")
    #myAcc.add_tracks_to("test0", song)
    return

if __name__ == "__main__":
    main()
