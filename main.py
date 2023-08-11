import os
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth



clscrt = os.environ["clscrt"]
clid = os.environ["clsid"]
scope = "playlist-modify-public playlist-modify-private ugc-image-upload"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clid,
                                               client_secret=clscrt,
                                               redirect_uri="https://localhost",
                                               scope=scope)
)

folder = os.listdir(r"D:\pypy\spotify\images")


for item in folder:
    with open(rf"D:\pypy\spotify\images/{item}","r",encoding="utf-8") as data:
        print(time.strftime("%H:%M"))
        if time.strftime("%H:%M") != "16:02":
            last = open(r"D:\pypy\spotify\last.txt","w+",encoding="utf-8")
            if item == last.read():
                try:
                    last.write(item)
                    last.close()
                    resim=rf"{data.read()}"
                    sp.playlist_upload_cover_image('5zRVoZ3TGDdVt7edDOqrb0',resim)
                    time.sleep(60)
                except Exception as error:
                    print(error)
            else:
                continue
        else:
            time.sleep(60)