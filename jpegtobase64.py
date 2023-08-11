import base64
import os

imgs = os.listdir(r"D:\pypy\spotify\images")

def convert(imgs):
    for img in imgs:
        if img.endswith("jpg"):
            with open(rf"D:\pypy\spotify\images\{img}","rb") as imgbase:
                base = base64.b64encode(imgbase.read()).decode("utf-8")
                dosya = open(rf"D:\pypy\spotify\images/{img}.txt","w")
                dosya.write(f"data:image/jpeg;base64,{str(base)}")
        else:
            pass
convert(imgs)