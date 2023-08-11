import os
import time

folder = os.listdir("images")
for item in folder:
    with open(f"images/{item}","r") as data:
        print(time.strftime("%H:%M"))
        if time.strftime("%H:%M"): #== "22:09":
            last = open("last.txt","w+")
            last.write(item)
            last.close()
            if folder.index(item) == folder.index(open("last.txt","r").read()):
                print(data.read())