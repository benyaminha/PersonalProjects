#quickly moves all files from usb to desginated file
import os
import shutil
from pathlib import Path

def prompt():
    global specificFolder
    global dest
    print("To which folder tho?")
    specificFolder = str(input())
    dest = "~/workspaces/" + specificFolder + "/"

src = "/Volumes/transit"
prompt()

while os.path.exists(dest) == False:
    print("Create new folder?") 
    if input() == 'y': 
        os.makedirs(dest)
    else: 
        prompt()

files = os.listdir(src)

if len(files) == 0:
    print("RUH ROH no files")
else:
    for f in files:
        if f != ".Spotlight-V100" and f != ".Trashes" and f != "System Volume Information":
            shutil.copy2(os.path.join(src, f), dest)
print("Done.")



