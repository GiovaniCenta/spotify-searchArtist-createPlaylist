### Goal: pick an artist name and create an playlist with all the songs i have from him or her in my spotify library
"""
1 - Create artist playlist
2 - Search and filter my library data
3 - Add artist song to the playlist
"""
from myData import mySpotifyData
import json
import requests
from extras import alreadyExists
#########NEED TO FINISH ADDSONG FUNCTION, EXTRAS TOO

class artistPlaylist:
    def __init__(self):
        self.id = mySpotifyData.Id
        self.playlistToken = mySpotifyData.plToken
        self.libraryToken = mySpotifyData.libToken
        self.artist = "Drake"

    def createPlaylist(self):
        playlistName = f"{self.artist} playlist"
        #flag = alreadyExists(playlistName)

        request_body = json.dumps({
            "name": playlistName,
            "description": f"Playlist of a program that I did in python that filters my liked songs from {self.artist} ",
            "public": True
        })

        query = f"https://api.spotify.com/v1/users/{self.id}/playlists"
        response = requests.post(
            url=query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.playlistToken}"
            }
        )
        print(response)
        response_json = response.json()


        # playlist id
        return response_json["id"]



        pass

    def searchArtist(self):

        playlistId = self.createPlaylist()
        response = requests.get(
            url=f"https://api.spotify.com/v1/me/tracks",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.libraryToken)
            }
        )

        print(response)
        print("\n\n")
        response_json = response.json()
        print(response_json)
        songs = (response_json.get("items"))
        print(songs)
        for song in songs:
            tracks = song['track']
            albums = tracks["album"]
            artists = albums["artists"]
            for artist in artists:
                #print(artist["name"])
                if artist["name"] == self.artist:
                    print(f"Oi {self.artist}")
                    uri = tracks["uri"]
                    self.addSong(uri,playlistId)








    def addSong(self,uri,playlistId):
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlistId)

        response = requests.post(
            query,
            data=uri,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.libraryToken)
            }
        )



if __name__ == '__main__':
    ap=artistPlaylist()
    print(ap.searchArtist())


