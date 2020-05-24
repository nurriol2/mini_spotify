#!/usr/bin/env python3

from account import SpotifyAccount

#spotipy.exceptions.SpotifyException

def main():

    #song = "one in a million dance gavin dance"
    #song = "88834738951135633371"
    myAcc = SpotifyAccount()
    r = myAcc.get_track_id(song)
    print(r)
    #myAcc.create_playlist("test0")
    #myAcc.add_tracks_to("test0", song)
    return

if __name__ == "__main__":
    main()
