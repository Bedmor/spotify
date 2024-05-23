import os

folder = os.listdir("images")
for item in folder:
    with open(f"images/{item}","r") as data:
        try:
            last = open("last.txt","w+")
            last.write(item)
            if folder.index(item) == last.read():
                print(data.read())
                last.close()
            else:
                last.close()
        except Exception as err:
            print(err)